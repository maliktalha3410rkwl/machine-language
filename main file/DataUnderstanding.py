class DataUnderstanding:
    def __init__(self, data):
        """Initialize with a pandas DataFrame"""
        self.data = data

    def overview(self):
        """ Display basic info and stats about the dataset"""
        print("Shape of the data:", self.data.shape)
        print("\nData types:\n", self.data.dtypes)
        print("\nMissing values:\n", self.data.isnull().sum())
        print("\nStatistical summary:\n", self.data.describe(include='all'))

    def unique_values(self, column):
        """Print unique values in a column"""
        unique_vals = self.data[column].unique()
        print(f"Unique values in '{column}':\n{unique_vals}")
        