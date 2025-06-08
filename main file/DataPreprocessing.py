class DataPreprocessing:
    def __init__(self, data):
        """ Initialize with a pandas DataFrame"""
        self.data = data

    def drop_columns(self, columns):
        """Drop specified columns from the dataset"""
        self.data = self.data.drop(columns=columns)

    def fill_missing_with_mean(self, columns):
        """Fill missing values in specified columns with mean"""
        for col in columns:
            mean_val = self.data[col].mean()
            self.data[col] = self.data[col].fillna(mean_val)

    def fill_missing_with_mode(self, columns):
        """Fill missing values in specified columns with mode"""
        for col in columns:
            mode_val = self.data[col].mode()[0]
            self.data[col] = self.data[col].fillna(mode_val)

    def encode_categorical(self, columns):
        """ Convert categorical columns to dummy/one-hot encoding"""
        self.data = pd.get_dummies(self.data, columns=columns)

    def normalize_columns(self, columns):
        """Normalize specified numeric columns (Min-Max scaling)"""
        for col in columns:
            min_val = self.data[col].min()
            max_val = self.data[col].max()
            self.data[col] = (self.data[col] - min_val) / (max_val - min_val)
