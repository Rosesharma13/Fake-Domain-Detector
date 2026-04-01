from src.train import train_model
from src.predict import predict

def main():
    model, vectorizer = train_model()

    print("\n=== Fake Domain Detector ===")

    while True:
        user_input = input("Enter domain (or 'exit'): ")

        if user_input.lower() == 'exit':
            break

        result = predict(user_input, model, vectorizer)
        print("Result:", result)

if __name__ == "__main__":
    main()
