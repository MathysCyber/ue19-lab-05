import requests
import sys

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print("--- Votre blague du jour ---")
        print(f"Q: {data['setup']}")
        print(f"A: {data['punchline']}")
        print("----------------------------")

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la connexion à l'API : {e}")
        sys.exit(1) 

if __name__ == "__main__":
    get_joke()