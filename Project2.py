
"""
DecodeLabs Internship - Project 2
Data Classification Using AI

This project trains a machine learning model
to classify flowers using the Iris dataset.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


def main():
    # 1. Load the dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    print("=" * 50)
    print("DECODELABS INTERNSHIP - PROJECT 2")
    print("DATA CLASSIFICATION USING AI")
    print("=" * 50)

    # 2. Understand the dataset
    print("\n1. DATASET INFORMATION")
    print("-" * 30)
    print(f"Total samples: {X.shape[0]}")
    print(f"Total features: {X.shape[1]}")
    print(f"Flower classes: {', '.join(iris.target_names)}")
    print(f"Feature names: {', '.join(iris.feature_names)}")

    # 3. Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("\n2. DATA SPLITTING")
    print("-" * 30)
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")

    # 4. Create and train the classification model
    model = make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=5)
    )

    model.fit(X_train, y_train)

    print("\n3. MODEL TRAINING")
    print("-" * 30)
    print("Algorithm: K-Nearest Neighbors (KNN)")
    print("Model trained successfully!")

    # 5. Test the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("\n4. MODEL EVALUATION")
    print("-" * 30)
    print(f"Test accuracy: {accuracy:.2%}")

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            labels=[0, 1, 2],
            target_names=iris.target_names,
            zero_division=0
        )
    )

    # 6. Predict the class of a new flower
    new_flower = [[5.1, 3.5, 1.4, 0.2]]
    prediction = model.predict(new_flower)[0]

    print("5. NEW FLOWER PREDICTION")
    print("-" * 30)
    print(f"Flower measurements: {new_flower[0]}")
    print(f"Predicted flower: {iris.target_names[prediction]}")

    print("\nProject completed successfully!")


if __name__ == "__main__":
    main()
