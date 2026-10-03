import requests

user_message = "What is virat Kohli's latest odi score"

request_message = {
    "message": user_message,
    "sessionId": "test-user-2"
}

url = "http://localhost:5678/webhook-test/d0a4028b-a1ad-445a-84a9-0d4d32d6b2b1"

response = requests.post(url, json=request_message)

print(response.status_code)
print(response.text)