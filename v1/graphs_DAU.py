import seaborn as sns
from matplotlib.dates import DateFormatter, AutoDateLocator
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import calendar
import getData


def DAU_plot() -> None:
    res = getData.DAU()

    df = pd.DataFrame(res, columns=["Date", "Users"])

    df["Date"] = pd.to_datetime(df["Date"])

    sns.set(style="whitegrid")
    plt.figure(figsize=(16, 8))
    ax = sns.lineplot(data=df, x="Date", y="Users")

    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    plt.xticks(rotation=45)

    #plt.title("Daily active users over 2016")
    ax.set_title('Daily Active Users through 2016', fontsize=17)
    #plt.xlabel("Date", fontsize=12, labelpad=50)
    #plt.ylabel("Users", fontsize=12, labelpad=10)

    ax.set_ylabel('Users', fontsize=14, labelpad=15) 
    ax.set_xlabel('')
    #plt.savefig(f"graphs/whole_year.png")
    plt.show()



def DAU_month(desired_month) -> None:

    res = getData.DAU()

    df = pd.DataFrame(res, columns=["Date", "Users"])

    df["Date"] = pd.to_datetime(df["Date"])

    df_filtered = df[df["Date"].dt.month == desired_month]

    sns.set(style="darkgrid")
    sns.lineplot(data=df_filtered, x="Date", y="Users")

    plt.xticks(rotation=45)

    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    plt.title(f"{calendar.month_name[desired_month]}")
    plt.xlabel("Date")
    plt.ylabel("Users")

    plt.show()



def DAU_month2(desired_month) -> None:

    res = getData.DAU()

    df = pd.DataFrame(res, columns=["Date", "Users"])
    df["Date"] = pd.to_datetime(df["Date"])
    df_filtered = df[df["Date"].dt.month == desired_month]

    # fig, ax = plt.subplots(figsize=(12, 6))
    sns.set(style="darkgrid")
    ax = sns.lineplot(data=df_filtered, x="Date", y="Users")

    plt.xticks(rotation=45)

    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.gca().xaxis.set_major_formatter(
        mdates.DateFormatter("%A"))  # ("%Y-%m-%d\n%A")

    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))


    ax.set_title(f"Time Series Plot of Users over {calendar.month_name[desired_month]}", fontsize=17)

    ax.set_ylabel('Users', fontsize=14, labelpad=15) 


    """
    plt.title(
        f"Time Series Plot of Users over {calendar.month_name[desired_month]}")
    plt.xlabel("Date")
    plt.ylabel("Users")
    """


    plt.show()
    # plt.savefig(f"v1/graphs/DAU_months/{calendar.month_name[desired_month]}.png")


def get_all_months() -> None:
    for i in range(12):
        DAU_month2(i+1)


def DAU_plot_6months() -> None:
    res = getData.DAU()

    df = pd.DataFrame(res, columns=["Date", "Users"])

    df["Date"] = pd.to_datetime(df["Date"])

    # Filter the first 6 months
    start_date = df["Date"].min()
    end_date = start_date + pd.DateOffset(months=6)
    df = df[(df["Date"] >= start_date) & (df["Date"] < end_date)]

    print(df)
    sns.set(style="darkgrid")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="Date", y="Users")

    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    plt.xticks(rotation=45)

    plt.title("Time Series Plot of Users over Dates")
    plt.xlabel("Date")
    plt.ylabel("Users")

    plt.savefig(f"v1/graphs/half_year.png")
    plt.show()

# DAU_plot_6months()


def DAU_month2(desired_month, desired_month_end) -> None:

    months = [i for i in range(desired_month, desired_month_end + 1)]

    res = getData.DAU()

    df = pd.DataFrame(res, columns=["Date", "Users"])
    df["Date"] = pd.to_datetime(df["Date"])
    df_filtered = df[df["Date"].dt.month.isin(months)]

    # fig, ax = plt.subplots(figsize=(12, 6))
    sns.set(style="whitegrid")
    plt.figure(figsize=(16, 8))
    ax =sns.lineplot(data=df_filtered, x="", y="Users")

    plt.xticks(rotation=45)
    plt.xticks(plt.xticks(rotation=45)[0][2:])

    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    
    #locator = mdates.WeekdayLocator(byweekday=(mdates.FR, mdates.SU))
    #formatter = mdates.DateFormatter('%A')
    #plt.gca().xaxis.set_major_locator(locator)
    #plt.gca().xaxis.set_major_formatter(formatter)

    # Skipping the first two labels

    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    #plt.title(
    #    f"Time Series Plot of Users over {calendar.month_name[desired_month]} - {calendar.month_name[desired_month_end]}")
    ax.set_title(f"Daily Active Users {calendar.month_name[desired_month]} - {calendar.month_name[desired_month_end]}", fontsize=17)
    
    """

    ax.set_ylabel('Users', fontsize=14, labelpad=15) 
    ax.set_xlabel("Weekdays marking pattern occurrence")"""
    #plt.xlabel("Date")
    #plt.ylabel("Users")

    plt.savefig(
       f"graphs/{calendar.month_name[desired_month]} - {calendar.month_name[desired_month_end]}.png")
    plt.show()

DAU_month2(6,9)

