class Visualizer:
    def __init__(self, data):
        self.data = data

    def plot_brand_distribution(self, column='Brand', width=10, height=6, rotation=45, title='Laptop Brand Distribution'):
        plt.figure(figsize=(width, height))
        sns.countplot(data=self.data, x=column, order=self.data[column].value_counts().index)
        plt.title(title)
        plt.xticks(rotation=rotation)
        plt.tight_layout()
        plt.show()

    def plot_price_vs_ram(self, x='RAM', y='Final Price', hue='Touch', width=8, height=6, title='Final Price vs RAM'):
        plt.figure(figsize=(width, height))
        sns.scatterplot(data=self.data, x=x, y=y, hue=hue)
        plt.title(title)
        plt.tight_layout()
        plt.show()

    def plot_cpu_price_box(self, x='CPU', y='Final Price', width=10, height=6, rotation=45, title='Price Distribution by CPU Type'):
        plt.figure(figsize=(width, height))
        sns.boxplot(data=self.data, x=x, y=y)
        plt.xticks(rotation=rotation)
        plt.title(title)
        plt.tight_layout()
        plt.show()

    def plot_storage_type_distribution(self, x='Storage type', hue='Storage type', width=6, height=4, palette='Set2', legend=False, title='Storage Type Distribution'):
        plt.figure(figsize=(width, height))
        sns.countplot(data=self.data, x=x, hue=hue, palette=palette, legend=legend)
        plt.title(title)
        plt.tight_layout()
        plt.show()

    def plot_touch_vs_price(self, x='Touch', y='Final Price', hue='Touch', palette=['skyblue', 'salmon'], legend=False, width=6, height=4, title='Price Comparison: Touch vs Non-Touch'):
        plt.figure(figsize=(width, height))
        sns.boxplot(data=self.data, x=x, y=y, hue=hue, palette=palette, legend=legend)
        plt.title(title)
        plt.tight_layout()
        plt.show()

    def plot_correlation_heatmap(self, width=8, height=6, cmap='coolwarm', annot=True, title='Correlation Heatmap'):
        plt.figure(figsize=(width, height))
        numeric_data = self.data.select_dtypes(include='number')
        sns.heatmap(numeric_data.corr(), annot=annot, cmap=cmap)
        plt.title(title)
        plt.tight_layout()
        plt.show()

    def plot_screen_size_distribution(self, column='Screen', bins=15, kde=True, width=8, height=5, title='Screen Size Distribution'):
        plt.figure(figsize=(width, height))
        sns.histplot(self.data[column], bins=bins, kde=kde)
        plt.title(title)
        plt.tight_layout()
        plt.show()

        