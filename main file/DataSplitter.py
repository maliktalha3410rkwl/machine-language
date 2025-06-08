class DataSplitter:
    def __init__(self, data, target_column):
        """Store the full dataset and target column"""
        self.data = data
        self.target_column = target_column

    def split(self, test_size=0.2, random_state=42):
        """Split the data into features (X) and target (y)"""
        X = self.data.drop(columns=[self.target_column])
        y = self.data[self.target_column]

        """Perform train-test split"""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

        """Store and return splits"""
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

        return X_train, X_test, y_train, y_test