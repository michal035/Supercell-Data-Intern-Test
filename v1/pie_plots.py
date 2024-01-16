import matplotlib.pyplot as plt
import seaborn as sns


def pie():
    labels = ['Android users', 'iOS users']
    sizes = [82, 18]

    custom_colors = sns.color_palette("PuRd", n_colors=6)

    plt.pie(sizes, labels=labels, autopct='%1.1f%%',
            startangle=90, colors=custom_colors)
    plt.title("Proportion of iOS and Android users")
    plt.axis('equal')

    plt.savefig(f"graphs/pie plots/Android_iOS_users_proportion.png")
    plt.show()


pie()


def bar():
    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    values = [15580, 9518, 8174, 9244]

    sns.set(style="whitegrid")
    plt.figure(figsize=(6, 4))
    plt.title("Revenue split into quarters")
    bar_width = 0.3

    custom_palette = sns.color_palette("Reds", n_colors=8)
    custom_palette = custom_palette[4:]

    ax = sns.barplot(x=categories, y=values,
                     palette=custom_palette, width=bar_width)

    plt.show()


def bar2():
    def color_mapping(val):
        if val > 5000:
            # return "#c9343e"
            return "#f5583d"
        elif val > 10000:
            return "#900C3F"
        else:
            return "#900C3F"

    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    values = [15580, 9518, 8174, 9244]

    sns.set(style="whitegrid")
    plt.figure(figsize=(6, 4))
    plt.title("Revenue split into quarters")
    bar_width = 0.3

    # Apply the color mapping function to generate a list of colors
    colors = [color_mapping(val) for val in values]

    # Create a bar plot using Seaborn with custom colors
    ax = sns.barplot(x=categories, y=values, palette=colors, width=bar_width)
    # plt.savefig(f"graphs/pie plots/Quarters_revenue.png")
    plt.show()
