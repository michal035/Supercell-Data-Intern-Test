import seaborn as sns
import matplotlib.pyplot as plt
import getData
import pandas as pd


def sales_by_countr():
    res = getData.geographic_split_of_revenue()
    df = pd.DataFrame(res, columns=["Country", "Value"])

    sns.set_style("white")

    def color_mapping(val):
        if val > 90000:
            return "#900C3F"
        elif val > 50000:
            return "#8d435c"
        else:
            return "#8d435c"

    df["Color"] = df["Value"].apply(color_mapping)

    plt.figure(figsize=(16, 8))
    sns.barplot(x="Country", y="Value", data=df, hue="Color",
                dodge=False, palette=["#900C3F", "#8d435c"], legend=False)
    plt.title("Bar Plot of Country Values", fontsize=16)
    plt.xlabel("Countries", fontsize=14)
    plt.ylabel("Values", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)

    plt.grid(axis="y", linestyle="--")
    plt.show()


def average_per_country():

    res = getData.average_per_country()
    df = pd.DataFrame(res, columns=["Country", "Value"])

    sns.set_style("darkgrid")

    plt.figure(figsize=(16, 8))
    sns.barplot(x="Country", y="Value", data=df, color='lightblue')
    plt.title("Bar Plot of Country Values", fontsize=16)
    plt.xlabel("Countries", fontsize=14)
    plt.ylabel("Values", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)

    plt.grid(axis="y", linestyle="--")
    plt.show()



