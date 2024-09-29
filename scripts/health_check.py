import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The application at {url} is up and running.")
        else:
            print(f"The application at {url} is down. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error checking the application health: {e}")

if __name__ == "__main__":
    app_url = "http://localhost:8081/"  # Replaced with url from problem statement 1
    check_application_health(app_url)
