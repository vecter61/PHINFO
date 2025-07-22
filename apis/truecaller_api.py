from truecallerpy import search_phonenumber
from config import load_config

config = load_config()
TOKEN = config.get("truecaller_token", "")

def query_truecaller(number, country_code="IN"):
    if not TOKEN:
        return {"Error": "Truecaller token not available."}

    try:
        data = search_phonenumber(number, country_code, TOKEN)
        user = data.get("data", {})
        return {
            "Name": user.get("name", "N/A"),
            "Email": user.get("internetAddresses", [{}])[0].get("id", "N/A"),
            "Gender": user.get("gender", "N/A"),
            "Country": user.get("addresses", [{}])[0].get("countryCode", "N/A")
        }
    except Exception as e:
        return {"Error": str(e)}
