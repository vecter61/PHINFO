import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def offline_lookup(number):
    try:
        parsed = phonenumbers.parse(number)
        return {
            "Valid": phonenumbers.is_valid_number(parsed),
            "Region": geocoder.description_for_number(parsed, "en"),
            "Carrier": carrier.name_for_number(parsed, "en"),
            "Timezones": ", ".join(timezone.time_zones_for_number(parsed))
        }
    except Exception as e:
        return {"Error": str(e)}
