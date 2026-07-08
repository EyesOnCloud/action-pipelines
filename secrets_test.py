import os

def main():
    environment = os.getenv("DEPLOY_ENV", "dev")
    api_key = os.getenv("API_KEY", "not_set")

    print(f"Running in environment: {environment}")
    print("Simulating API request using key: ****")  

if __name__ == "__main__":
    main()
