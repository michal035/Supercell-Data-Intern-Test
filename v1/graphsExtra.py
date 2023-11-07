import seaborn as sns
from matplotlib.dates import DateFormatter, AutoDateLocator
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import calendar
import getData


def DAU_plot() -> None:
    res = getData.DAU_by_country("CN")
    df = pd.DataFrame(res, columns=["Date", "Users"])
    df["Date"] = pd.to_datetime(df["Date"])


    res2 = getData.DAU()
    df2 = pd.DataFrame(res2, columns=["Date", "Users"])
    df2["Date"] = pd.to_datetime(df2["Date"])



    sns.set(style="whitegrid")
    plt.figure(figsize=(16, 8))

    ax = sns.lineplot(data=df2, x="Date", y="Users", color=(0, 0, 0.5), label='Global DAU')
    sns.lineplot(data=df, x="Date", y="Users", color=(0.5, 0, 0), label='China DAU')
    


    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

    plt.xticks(rotation=45)

    #plt.title("Daily active users in China and Word")
    ax.set_title("Daily active users in China and Word for July - September", fontsize=17)
    plt.xlabel(" ", fontsize=12, labelpad=50)
    plt.ylabel("Users", fontsize=12, labelpad=10)

            #ax.set_ylabel('Users', fontsize=14, labelpad=15) 

    #plt.savefig(f"v1/graphs/whole_year_for_china_and_world.png")
    plt.show()

#DAU_plot()




def DAU_plot2() -> None:
    #res = getData.DAU_by_country("CN")
    #df = pd.DataFrame(res, columns=["Date", "Users"])
    #df["Date"] = pd.to_datetime(df["Date"])


    #res2 = getData.DAU()
    #df2 = pd.DataFrame(res2, columns=["Date", "Users"])
    #df2["Date"] = pd.to_datetime(df2["Date"])


    res3 = getData.DAU_by_country("FR")
    df3 = pd.DataFrame(res3, columns=["Date", "Users"])
    df3["Date"] = pd.to_datetime(df3["Date"])


    res4 = getData.DAU_by_country("RU")
    df4 = pd.DataFrame(res4, columns=["Date", "Users"])
    df4["Date"] = pd.to_datetime(df4["Date"])

    res5 = getData.DAU_by_country("KR")
    df5 = pd.DataFrame(res5, columns=["Date", "Users"])
    df5["Date"] = pd.to_datetime(df5["Date"])



    sns.set(style="whitegrid")
    plt.figure(figsize=(16, 8))

    #ax = sns.lineplot(data=df2, x="Date", y="Users", color=(0, 0, 0.5), label='Global DAU')
    #sns.lineplot(data=df, x="Date", y="Users", color=(0.5, 0, 0), label='China DAU')
    ax = sns.lineplot(data=df3, x="Date", y="Users", color=(0, 0, 0.5), label='France DAU')
    sns.lineplot(data=df4, x="Date", y="Users", color=(0.5, 0, 0), label='Russia DAU')
    sns.lineplot(data=df5, x="Date", y="Users", color=(0.5, 0, 0.5), label='South Korea DAU')

    


    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

    plt.xticks(rotation=45)

    #plt.title("Daily active users in ... and Word")
    ax.set_title("Daily active users in France, Russia and South Korea for 2016", fontsize=17)
    plt.xlabel(" ", fontsize=12, labelpad=50)
    plt.ylabel("Users", fontsize=12, labelpad=10)

            #ax.set_ylabel('Users', fontsize=14, labelpad=15) 

    #plt.savefig(f"v1/graphs/whole_year_for_china_and_world.png")
    plt.show()







def DAU_plot3() -> None:

    months = [i for i in range(6, 9 + 1)]


    res = getData.DAU_by_country("CN")
    df = pd.DataFrame(res, columns=["Date", "Users"])
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[df["Date"].dt.month.isin(months)]

    res2 = getData.DAU()
    df2 = pd.DataFrame(res2, columns=["Date", "Users"])
    df2["Date"] = pd.to_datetime(df2["Date"])
    df2 = df2[df2["Date"].dt.month.isin(months)]



    sns.set(style="whitegrid")
    plt.figure(figsize=(16, 8))

    ax = sns.lineplot(data=df2, x="Date", y="Users", color=(0, 0, 0.5), label='Global DAU')
    sns.lineplot(data=df, x="Date", y="Users", color=(0.5, 0, 0), label='China DAU')
    


    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

    plt.xticks(rotation=45)

    #plt.title("Daily active users in China and Word")
    ax.set_title("Daily active users in China and Word for July - September", fontsize=17)
    plt.xlabel(" ", fontsize=12, labelpad=50)
    plt.ylabel("Users", fontsize=12, labelpad=10)

            #ax.set_ylabel('Users', fontsize=14, labelpad=15) 

    #plt.savefig(f"v1/graphs/whole_year_for_china_and_world.png")
    plt.show()


