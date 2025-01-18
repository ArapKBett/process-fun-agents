import requests

def send_fun_fact():
    response = requests.get('https://api.example.com/funfact')
    fun_fact = response.json().get('fact')
    print(f"Fun Fact: {fun_fact}")
    return fun_fact
