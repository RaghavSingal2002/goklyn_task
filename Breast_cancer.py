
# 1. Import Necessary Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings

# Suppress harmless sklearn warnings related to solver choice and future versions
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=UserWarning)

def run_classification_model(file_path='breast-cancer.csv'):
    """
    Executes the full Machine Learning workflow for the Breast Cancer dataset:
    Loading, Preprocessing, Splitting, Scaling, Training, and Evaluation.
    """
    try:
        # --- 2. Data Loading ---
        print("--- 1. Data Loading and Initial Cleanup ---")
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully from '{file_path}'. Shape: {df.shape}")

        # Drop non-predictive columns: 'id' and 'Unnamed: 32' (often a null column)
        df = df.drop(['id', 'Unnamed: 32'], axis=1, errors='ignore')

        # --- 3. Data Preprocessing: Target Encoding ---
        # Encode the target variable ('diagnosis'): M=Malignant, B=Benign
        le = LabelEncoder()
        # Convert 'M' and 'B' into numerical values: 0 and 1
        df['diagnosis'] = le.fit_transform(df['diagnosis']) 
        target_names_map = {0: 'Benign', 1: 'Malignant'}

        # Separate features (X) and target (y)
        X = df.drop('diagnosis', axis=1).values
        y = df['diagnosis'].values
        print(f"Features (X) shape: {X.shape}, Target (y) shape: {y.shape}")
        print(f"Target classes mapped: {target_names_map}")


        # --- 4. Data Splitting and Scaling ---
        print("\n--- 2. Splitting and Feature Scaling ---")

        # Split data: 80% train, 20% test. Use stratification to maintain class ratio.
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # Initialize and apply StandardScaler
        scaler = StandardScaler()

        # Fit scaler on training data (preventing data leakage) and transform both sets
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        
        print(f"Split completed: Training samples={X_train.shape[0]}, Testing samples={X_test.shape[0]}")
        # [Image of diagram illustrating a Python script file and a data CSV file in the same folder] 
        # Note: If the file path error persists, please ensure 'breast-cancer.csv' is in the same directory as this script!


        # --- 5. Model Training ---
        print("\n--- 3. Training Logistic Regression Model ---")

        # Initialize the Logistic Regression model
        # solver='liblinear' is efficient for small datasets and binary problems
        model = LogisticRegression(random_state=42, solver='liblinear', max_iter=1000)

        # Train the model on the scaled training data
        model.fit(X_train, y_train)

        print("Model training complete.")


        # --- 6. Model Evaluation ---
        print("\n--- 4. Model Evaluation on Test Set ---")

        # Make predictions
        y_pred = model.predict(X_test)

        # 6a. Overall Accuracy
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Overall Accuracy: {accuracy:.4f}\n")

        # 6b. Confusion Matrix
        conf_matrix = confusion_matrix(y_test, y_pred)
        print("Confusion Matrix (Actual vs. Predicted):")
        print(pd.DataFrame(conf_matrix, 
                           index=[f'Actual {target_names_map[0]}', f'Actual {target_names_map[1]}'], 
                           columns=[f'Pred {target_names_map[0]}', f'Pred {target_names_map[1]}']))

        # 6c. Detailed Classification Report (Precision, Recall, F1-Score)
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, target_names=['Benign', 'Malignant']))

    except FileNotFoundError:
        print(f"\n[FATAL ERROR] File not found. Please ensure '{file_path}' is in the correct directory.")
    except Exception as e:
        print(f"\n[CRITICAL ERROR] An unexpected error occurred: {e}")

# Execute the main function
if __name__ == "__main__":
    run_classification_model()

