import seaborn as sns
import matplotlib.pyplot as plt
import getData
import geopandas as gpd
import pandas as pd
import pycountry
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap



def sales_by_country():
    res = getData.geographic_split_of_revenue()
    df = pd.DataFrame(res, columns=["Country", "Revenue (USD)"])

    sns.set(style="whitegrid")
    # sns.set_style("white")

    def color_mapping(val):
        if val > 5000:
            return "#8d435c"
        elif val > 20000:
            return "#900C3F"
        else:
            return "#900C3F"

    df["Color"] = df["Revenue (USD)"].apply(color_mapping)

    plt.figure(figsize=(16, 8))
    sns.barplot(x="Country", y="Revenue (USD)", data=df, hue="Color",
                dodge=False, palette="Reds", legend=False)
    plt.title("Revenue Split across Markets (USD)", fontsize=17)
    plt.xlabel("Country Codes", fontsize=14)
    plt.ylabel("Revenue (USD)", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)

    plt.grid(axis="y", linestyle="-")

    # ax.set_title(f"Revenue Split Across Markets", fontsize=17)

    # ax.set_ylabel('Users', fontsize=14, labelpad=15)

    #plt.savefig(f"graphs/Sales/revenue_split.png")

    plt.show()





def convert_to_iso_a3(country_code):
    try:
        return pycountry.countries.get(alpha_2=country_code).alpha_3
    except (AttributeError, LookupError):
        return None


def Sales_by_country_map():

    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    fig, ax = plt.subplots(figsize=(16, 8))
    res = getData.geographic_split_of_revenue()
    df = pd.DataFrame(res, columns=["iso_a3", "Revenue (USD)"])
    df['iso_a3'] = df['iso_a3'].apply(convert_to_iso_a3)
    df = df.sort_values("Revenue (USD)")

    
    merge = world.merge(df, on='iso_a3')
    

    """country_codes = getData.country_codes()
    df_country_codes = pd.DataFrame(country_codes, columns=["iso_a3"])
    df_country_codes['iso_a3'] = df_country_codes['iso_a3'].apply(convert_to_iso_a3)
    df_country_codes['Revenue (USD)'] = 0.25
    df = df.combine_first(df_country_codes)"""

    #cmap = LinearSegmentedColormap.from_list("", ["lightblue", "darkred"])
    #Oranges, OrRD
    cmap = "Reds"
    # colors = [ 'indianred', 'darkred']
    # cmap = ListedColormap(colors)

    # merge['Revenue (USD)'] = merge['Revenue (USD)'].fillna('gray')
    merge.plot(column='Revenue (USD)', cmap=cmap, legend=True, ax=ax)

    # merge.loc[merge['Revenue (USD)'] == 0.25, 'color'] = 'grey'

    plt.title('Revenue split accros Markets (USD)', fontsize=17)
    
    #plt.savefig(f"graphs/Sales/revenue_split_map.png")
    plt.show()




def average_per_user_per_country_map():
    res_count, res_sum = getData.average_per_country()
    print(res_count[0])
    df = pd.DataFrame(res_count, columns=["iso_a3", "Account count"])
    df2 = pd.DataFrame(res_sum, columns=["iso_a3", "Accounts sum"])

    merged_df = pd.merge(df, df2, on="iso_a3", how="right")

    merged_df = merged_df.fillna(0)

    merged_df["Average"] = round(
        merged_df["Accounts sum"] / merged_df["Account count"], 2)
    


    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    fig, ax = plt.subplots(figsize=(16, 8))
    merged_df['iso_a3'] = merged_df['iso_a3'].apply(convert_to_iso_a3)
    merged_df = merged_df.sort_values("Average")

    
    merge = world.merge(merged_df, on='iso_a3')
    

    cmap = LinearSegmentedColormap.from_list("", ["lightblue", "darkred"])
    #Oranges, OrRD PuRd
    cmap = "OrRD"

    vmin, vmax = 0, 150
    merge.plot(column='Average', cmap=cmap, vmin=vmin, vmax=vmax, legend=False, ax=ax)


    plt.title('Revenue per User per Market', fontsize=17)
    #plt.savefig(f"graphs/Sales/revenue_per_user_map.png")
    plt.show()



def average_per_user_per_country():
    res_count, res_sum = getData.average_per_country()
    df = pd.DataFrame(res_count, columns=["iso_a3", "Account count"])
    df2 = pd.DataFrame(res_sum, columns=["iso_a3", "Accounts sum"])

    merged_df = pd.merge(df, df2, on="iso_a3", how="right")

    merged_df = merged_df.fillna(0)

    merged_df["Accounts sum"] = merged_df["Accounts sum"] / 100
    merged_df["Average"] = round(
        merged_df["Accounts sum"] / merged_df["Account count"], 2)


        
    merged_df = merged_df.sort_values("Average")
    print(merged_df)

    plt.figure(figsize=(14, 7))
    sns.barplot(x="iso_a3", y="Average", data=merged_df, color='moccasin')
    plt.title("Revenue per User per Country", fontsize=17)
    plt.xlabel("Countries", fontsize=14)
    plt.ylabel("Average Revenue per User (USD)", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)

    plt.grid(axis="y", linestyle="-")
    #plt.savefig(f"graphs/Sales/average_per_country_per_user_bar_plot.png")
    plt.show()




def split_of_user_per_country_map():
    res_count, res_not_used = getData.average_per_country()

    df = pd.DataFrame(res_count, columns=["iso_a3", "Account count"])
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    fig, ax = plt.subplots(figsize=(16, 8))
    df['iso_a3'] = df['iso_a3'].apply(convert_to_iso_a3)
    
    merge = world.merge(df, on='iso_a3')
    

    cmap = LinearSegmentedColormap.from_list("", ["lightblue", "darkred"])
    #Oranges, OrRd PuRd
    cmap = "PuRd"

    merge.plot(column='Account count', cmap=cmap, legend=True, ax=ax)


    plt.title('Geographic split of Users', fontsize=17)

    #plt.savefig(f"graphs/Sales/geographic_split_of_user_map.png")
    plt.show()




def average_per_country():

    res, res2 = getData.average_per_country()
    df = pd.DataFrame(res, columns=["Country", "Value"])

    sns.set_style("darkgrid")

    plt.figure(figsize=(14, 7))
    sns.barplot(x="Country", y="Value", data=df, color='lightblue')
    plt.title("Bar Plot of Country Values", fontsize=16)
    plt.xlabel("Countries", fontsize=14)
    plt.ylabel("Values", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)

    plt.grid(axis="y", linestyle="-")
    plt.show()



def time_sales():

    res = getData.time_sales()
    
    df = pd.DataFrame(res, columns=['date', 'value'])

    df['date'] = df['date'].str[:10]
    #df['date'] = pd.to_datetime(df['date'])


    #df = df.groupby('date')

    df['date'] = pd.to_datetime(df['date'])

    # Group by 'date' and apply sum to 'nvalue'
    result = df.groupby(df['date'].dt.to_period('M'))['value'].sum() / 100

    print(result)

    """sns.set_style("whitegrid")

    plt.figure(figsize=(14, 7))
    sns.barplot(x="date", y="value", data=df)#, color='lightblue')
    plt.title("Bar Plot of Country Values", fontsize=16)
    plt.xlabel("Countries", fontsize=14)
    plt.ylabel("Values", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)"""

    #plt.gca().get_yaxis().get_major_formatter().set_scientific(False)

    """plt.grid(axis="y", linestyle="-")
    plt.show()
    """

time_sales()