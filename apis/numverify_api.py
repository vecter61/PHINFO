import requests
from config import load_config

config = load_config()
API_KEY = config.get("numverify_api_key", "")

def query_numverify(phone):
    if not API_KEY:
        return {"Error": "NumVerify API key not available."}

    url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={phone}&format=1"
    try:
        r = requests.get(url).json()
        return {
            "Valid": r.get("valid"),
            "Country": r.get("country_name"),
            "Region": r.get("location"),
            "Carrier": r.get("carrier"),
            "Line Type": r.get("line_type")
        }
    except Exception as e:
        return {"Error": str(e)}
