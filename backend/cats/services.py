import requests

CAT_API_URL = "https://api.thecatapi.com/v1/breeds"


def validate_breed_func(breed_name: str) -> bool:
    try:
        response = requests.get(CAT_API_URL)

        if response.ok:
            breeds = response.json()

            for b in breeds:
                if b["name"].lower() == breed_name.lower():
                    return True
    except Exception as e:
        print(f"Error while getting breeds: {e}")
        return False
