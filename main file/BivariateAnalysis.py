class BivariateAnalysis:
    def __init__(self, data):
        # Initialize with a pandas DataFrame
        self.data = data

    def scatter_plot(self, x, y, width=6, height=4, point_color='b', title=None, xlabel=None, ylabel=None):
        """ Scatter plot for numeric vs numeric"""
        plt.figure(figsize=(width, height))
        sns.scatterplot(x=self.data[x], y=self.data[y], color=point_color)
        plt.title(title or f'{x} vs {y}')
        plt.xlabel(xlabel or x)
        plt.ylabel(ylabel or y)
        plt.show()    
  
    def box_plot(self, x, y, width=8, height=5, box_color='lightblue', rotation=45, title=None):
        """ Box plot for categorical vs numeric"""
        plt.figure(figsize=(width, height))
        sns.boxplot(x=self.data[x], y=self.data[y], color=box_color)
        plt.title(title or f'{y} by {x}')
        plt.xticks(rotation=rotation)
        plt.show()


    def correlation_heatmap(self, width=8, height=6, cmap='coolwarm', fmt=".2f", annot=True, title='Correlation Heatmap'):
        """Correlation heatmap for numeric columns"""
        plt.figure(figsize=(width, height))
        corr = self.data.corr(numeric_only=True)
        sns.heatmap(corr, annot=annot, cmap=cmap, fmt=fmt)
        plt.title(title)
        plt.show()

        