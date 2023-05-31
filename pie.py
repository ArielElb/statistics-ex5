import pandas as pd
import matplotlib.pyplot as plt

def plot_pie_chart(data, title, threshold, colors):
    counts = data.value_counts()
    other = counts[counts / counts.sum() < threshold]
    counts = counts.drop(other.index)
    counts['Other'] = other.sum()

    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', colors=colors)
    plt.title(title)

def plot_pie_charts(data_file):
    df = pd.read_csv(data_file)
    publisher_counts = df['publisher']
    society_counts = df['society']
    field_counts = df['field']

    plt.figure(figsize=(15, 5))

    # Publisher Pie Chart
    plt.subplot(1, 3, 1)
    publisher_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFFF99', '#FFCC99', '#FF99FF']
    plot_pie_chart(publisher_counts, 'Journal Publishers', 0.03, publisher_colors)

    # Society Pie Chart
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 2)
    society_colors = ['#FF99CC', '#66CCFF', '#99FFCC', '#FFFF99', '#FFCC99', '#FF99FF']
    plot_pie_chart(society_counts, 'Journal Societies', 0.005, society_colors)

    # Field Pie Chart
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 3)
    field_colors = ['#FF99CC', '#66CCFF', '#99FFCC', '#FFFF99', '#FFCC99', '#FF99FF']
    plot_pie_chart(field_counts, 'Journal Fields', 0.05, field_colors)

    plt.show()

plot_pie_charts('Journals.csv')
