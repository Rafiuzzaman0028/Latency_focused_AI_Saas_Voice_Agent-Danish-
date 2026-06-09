import requests

url = "http://localhost:8001/api/login"
resp = requests.post(url, json={"username": "admin", "password": "admin123"})
token = resp.json().get("access_token")

url = "http://localhost:8001/api/create-assistant"
headers = {"Authorization": f"Bearer {token}"}
data = {
    "assistant_name": "Test",
    "model": "gemini",
    "voice_id": "test",
    "language": "da"
}

print("Testing without files...")
resp = requests.post(url, headers=headers, files={"assistant_name": (None, "Test"), "model": (None, "gemini"), "voice_id": (None, "test"), "language": (None, "da")})
print(resp.status_code)
print(resp.json())
