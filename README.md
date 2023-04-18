
## Installation
```
git clone https://github.com/Mousumi44/bard-api
cd bard-api
pip install -r requirements.txt
```

## Authentication
Go to https://bard.google.com/

- F12 for console
- Copy the values
  - Session: Go to Application → Cookies → `__Secure-1PSID`. Copy the value of that cookie.


Open `.env` file in bard-api directory and put tokens there

```
BARD_TOKEN=<your token>
```


## Running
After adding needed tokens in .env start your bot by command:
```
python bard.py
```

## Credits
[github.com/acheong08/Bard](https://github.com/acheong08/Bard)
