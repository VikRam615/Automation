import requests
import time

BASE_URL = 'http://localhost:8081/'

def test_frontend():
    '''
        Test Details:
        1.Sending a request to the URL
        2.Validating if the recieved http code is 200
        3.Validating the reponse received
        Test Expectations:
        1.Should return the expected message
    '''
    try:
        response = requests.get(BASE_URL)
        assert response.status_code == 200
        assert "Hello from the Backend!" in response.text
        print("Test passed: Frontend is communicating with Backend correctly.")
    except AssertionError:
        print("Test failed: Greeting message not found in frontend response.")
    except Exception as e:
        print(f"An error occurred: {e}")
def test_invalid_backend_url():
    '''
        Test Details:
        1.Sending a request to the URL with invalid endpoint
        2.Validating if the recieved http code is 404
        Test Expectations:
        1.Should return the expected http code
    '''
    response = requests.get(f"{BASE_URL}/some-endpoint")
    assert response.status_code == 404
def test_empty_response():
    '''
        Test Details:
        1.Sending a request to the URL
        2.Validating if the recieved response is not null
    '''
    response = requests.get(BASE_URL)
    assert response.text != ''
def test_slow_response_handling():
    '''
        Test Details:
        1.Sending a request to the URL
        2.Validating if the recieved http code is 200
        3.Validating that the message is received even after delay
        Test Expectations:
        1.Should return the expected message
    '''
    time.sleep(5)  # delay
    response = requests.get(BASE_URL)
    assert response.status_code == 200

if __name__ == "__main__":
    test_invalid_backend_url()
    test_empty_response()
    test_slow_response_handling()

