class UnivariateAnalysis:
    def __init__(self, data):
        """Initialize with a pandas DataFrame"""
        self.data = data

    def describe_column(self, column):
        """Print basic statistics of a column"""
        print(self.data[column].describe())

    def plot_numeric(self, column, bins=30, hist_color='skyblue', box_color='lightgreen',
                 fig_width=12, fig_height=5, subplot_row1=1, subplot_col1=2, index1=1,
                 subplot_row2=1, subplot_col2=2, index2=2):
        plt.figure(figsize=(fig_width, fig_height))

        plt.subplot(subplot_row1, subplot_col1, index1)
        sns.histplot(self.data[column], kde=True, bins=bins, color=hist_color)
        plt.title(f'Distribution of {column}')

        plt.subplot(subplot_row2, subplot_col2, index2)
        sns.boxplot(x=self.data[column], color=box_color)
        plt.title(f'Boxplot of {column}')

        plt.tight_layout()
        plt.show()

        
    def plot_categorical(self, column, hue=None, palette='Set2', legend=False, width=6, height=4, rotation=45):
        plt.figure(figsize=(width, height))
        sns.countplot(data=self.data, x=column, hue= column, palette=palette, legend=legend)
        plt.title(f'Frequency of {column}')
        plt.xticks(rotation=rotation)
        plt.show()


        