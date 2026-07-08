import requests
  
# Get a random joke
response = requests.get("https://official-joke-api.appspot.com/random_joke")
  
if response.status_code == 200:
    print("I was able to connect to the API no problem.")
    joke = response.json()
    print(f"{joke['setup']} {joke['punchline']}")
else:
    print("Something went wrong. This is not a joke.")
