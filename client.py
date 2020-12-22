import requests
import json

def post_data():
    data = {
            "first": "Eva",
            "last": "Svensson",
            "things": [
               {
                   "things_name": "First thing",
                   "thing_price": 23
               },
               {
                   "things_name": "Second thing",
                   "thing_price": 45
               }
           ]
    }
    r = requests.post('http://127.0.0.1:5000', json=data)
    response_data = json.loads(r.text)
    print()

def main():
    name = input("What is your name? ")
    url = f"https://api.agify.io/?name={name}"
    resp = requests.get(url)
    data = json.loads(resp.text)
    print(f"Hello {name}!")
    print(f"I think you are {data['age']} years old")


if __name__ == '__main__':
    main()
