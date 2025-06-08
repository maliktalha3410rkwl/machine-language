class ModelTrainer:
    def __init__(self):
        self.model = SVR()
        print("🤖 SVR model created.")

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        print("✅ Model training complete.")

    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        print("📉 Evaluation Metrics:")
        print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
        print(f"R² Score: {r2_score(y_test, y_pred):.2f}")

    def get_model(self):
        return self.model
    
   