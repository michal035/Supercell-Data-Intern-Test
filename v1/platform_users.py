import seaborn as sns
import matplotlib.pyplot as plt
import getData
import geopandas as gpd
import pandas as pd
import pycountry
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap


def convert_to_iso_a3(country_code):
    try:
        return pycountry.countries.get(alpha_2=country_code).alpha_3
    except (AttributeError, LookupError):
        return None


def DAU_plot() -> None:
    all, ios, an = getData.get_platform_data()
    df = pd.DataFrame(all, columns=["iso_a3", "Users"])
    ios = pd.DataFrame(ios, columns=["iso_a3", "Users_iOS"])
    an = pd.DataFrame(an, columns=["iso_a3", "An"])

    df = df.merge(ios, on="iso_a3")
    df = df.merge(an, on="iso_a3")
    df["An"] = df["An"] * (-1)
    df["balance"] = (df["Users_iOS"] / df["Users"])*100

    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    fig, ax = plt.subplots(figsize=(16, 8))
    df['iso_a3'] = df['iso_a3'].apply(convert_to_iso_a3)

    merge = world.merge(df, on='iso_a3')

    cmap = LinearSegmentedColormap.from_list("", ["lightblue", "darkred"])
    cmap = "PuRd"

    merge.plot(column='balance', cmap=cmap, legend=True, ax=ax)

    plt.title('Geographic split of iOS user', fontsize=17)

    # plt.savefig(f"graphs/geographic_split_of_ios_users_map.png")
    plt.show()


DAU_plot()
