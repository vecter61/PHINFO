#📞 PHINFO — Advanced Phone Number Intelligence Tool

PHINFO is a powerful and modular **Python CLI tool** that allows you to extract detailed metadata about international phone numbers using both **offline libraries** and **real-time public APIs**. Designed for ethical research and educational use, it provides insights like:

- Validity
- Carrier and region
- Number type (mobile/landline)
- Owner name (via Truecaller token, personal use only)
- Bulk or single-number analysis

---

## 🚀 Features

✅ Offline analysis using [Google's phonenumbers library](https://github.com/daviddrysdale/python-phonenumbers)  
✅ Public API integrations (optional and user-controlled)  
✅ Auto-prompts to save API keys once  
✅ Respects privacy laws — only uses public and authorized endpoints  
✅ Works even if some APIs are not configured  
✅ Modular and extensible architecture

---

## 🔧 Installation

```bash
git clone https://github.com/yourusername/phinfo.git
```
```bash
cd phinfo
```
```bash
pip install -r requirements.txt
```
📦 Requirements
Python 3.7+


Modules:

phonenumbers

requests

rich

truecallerpy (optional)

```bash

🗝️ API Key Setup (Auto-Prompted)
PHINFO supports up to 3 APIs. You will be prompted for these keys on first run:

API	Free Limit	Get It From
Abstract API	1000/month	https://www.abstractapi.com/phone-validation-api
NumVerify	250/month	https://numverify.com
Truecaller	No public API	https://github.com/sumitrathi/truecallerpy
```

Keys are saved to a config.json file and reused securely.

⚠️ If you skip an API key, PHINFO will still work with available ones.

📌 Usage
🔍 Single Number Lookup
```bash
python phinfo.py
```
You'll be prompted to enter:

Country code (e.g. IN, US, GB)

Local phone number (without country code)
```bash

Example input:
Country Code: IN
Phone Number: 9876543210
📁 Optional Bulk Mode (coming soon)
Add a list of numbers to bulk.txt for batch processing.

```
🧠 What PHINFO Reveals
```bash

Type	Data Example	Source
Validity	✅ Valid or ❌ Invalid	phonenumbers
Carrier	Airtel, Verizon, Vodafone, etc.	Abstract/NumVerify
Region	Maharashtra, California, etc.	All
Timezones	Asia/Kolkata, US/Pacific	phonenumbers
Line Type	Mobile / Landline	Abstract
Owner Name	John Doe (if available)	Truecaller (optional)
```
```bash

📂 Project Structure
PHINFO/
├── apis/
│   ├── abstract_api.py
│   ├── numverify_api.py
│   └── truecaller_api.py
├── config.py
├── core.py
├── phinfo.py
├── config.json           # Auto-generated
├── bulk.txt              # (optional)
├── requirements.txt
└── README.md
```
⚠️ Legal Disclaimer
PHINFO is intended strictly for educational and personal research purposes.
Using APIs like Truecaller beyond personal access may violate terms of service or data protection laws in your region.

By using this tool, you agree to take full responsibility for how you use it.

🙌 Credits
phonenumbers (Google)

TruecallerPy (by @sumitrathi)

Abstract API

NumVerify (API Layer)

Rich (CLI Styling)
```bash
🛠️ License
This project is released under the MIT License.
You are free to use, modify, and distribute — with proper attribution and respect for data policies.
```
Support / Donations

If you find PHINFO useful, consider supporting the project via Bitcoin:
```bash
bc1qlpw590fkykfdd9v92g9snfmx8hc8vwxvkz5npm
```