import requests
from config import load_config

config = load_config()
API_KEY = config.get("abstract_api_key", "")

def query_abstract(phone):
    if not API_KEY:
        return {"Error": "Abstract API key not available."}

    url = f"https://phonevalidation.abstractapi.com/v1/?api_key={API_KEY}&phone={phone}"
    try:
        r = requests.get(url).json()
        return {
            "Valid": r.get("valid"),
            "Country": r.get("country", {}).get("name"),
            "Region": r.get("location"),
            "Carrier": r.get("carrier"),
            "Line Type": r.get("line_type")
        }
    except Exception as e:
        return {"Error": str(e)}
