import pandas as pd
import matplotlib.pyplot as plt

def plot_histogram(data_file, variable, title, num_bins, color):
    df = pd.read_csv(data_file)
    plt.figure(figsize=(8, 6))
    plt.hist(df[variable], bins=num_bins, edgecolor='black', color=color)
    plt.xlabel(variable)
    plt.ylabel('Frequency')
    plt.title(title)
    plt.show()

data_file = 'Journals.csv'
variables = ['price', 'pages', 'charpp', 'citations', 'foundingyear', 'subs']
titles = ['Price Distribution', 'Pages Distribution', 'Characters per Page Distribution',
          'Citations Distribution', 'Founding Year Distribution', 'Subscriptions Distribution']
num_bins = [20, 25, 20, 10, 10, 20]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFFF99', '#FFCC99', '#FF99FF']

for i in range(len(variables)):
    plot_histogram(data_file, variables[i], titles[i], num_bins[i], colors[i])
