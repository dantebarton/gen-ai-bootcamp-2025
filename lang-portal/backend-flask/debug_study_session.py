import requests
import json

# URL of the API endpoint
url = 'http://localhost:5001/api/study-sessions'

# Prepare the same data as in the failing test
payload = {
    "group_id": 1,
    "activity_id": 2,
    "end_time": "2023-10-10T10:00:00",
    "review_items": [
        {"item_id": 1, "status": "correct"},
        {"item_id": 2, "status": "wrong"}
    ]
}

# Set the content type to application/json
headers = {'Content-Type': 'application/json'}

try:
    # Make the POST request
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    # Print status code
    print(f"Status Code: {response.status_code}")
    
    # Print headers
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
    
    # Print body
    print("\nResponse Body:")
    try:
        # Try to parse and print as JSON for better readability
        print(json.dumps(response.json(), indent=4))
    except:
        # If not JSON, print raw text
        print(response.text)
        
except Exception as e:
    print(f"Error making request: {e}")

print("\nNote: Ensure the Flask server is running before executing this script.")

