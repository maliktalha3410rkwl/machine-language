class DataCollector:
    def __init__(self, source_path):
        self.source_path = "laptops.csv"
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.source_path)
        print(f"Data loaded successfully from {self.source_path}")
        return self.data

    def get_data_summary(self):
        if self.data is None:
            print("Data not loaded yet. Please run load_data() first.")
            return
        print("Data Info:")
        print(self.data.info())
        print("\nFirst 5 rows:")
        print(self.data.head())
        