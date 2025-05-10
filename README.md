# GEOGUESSR-CHALLENGE-AUTO-SCORER

This repo aims to obtain a table with the list of scores for all participants of a Geoguessr challenge.
Then, if multiple challenges are provided, create a ranked list.

Originally, it made use of python module: https://pypi.org/project/geoguessr/0.0.2/ .
Which comes from Github code: https://github.com/jaceiverson/geoguessr/tree/master .

However, the module is **outdated** and the original API endpoints don't work anymore. I had to reverse-engineer the (currently) correct endpoints and redo the Pandas-handling part because the JSON shape seems to look different than in the original endpoint. In the end, decided to replace most of the Pandas with DuckDB to make the data-handling part look fancy with SQL.

## Development notes:
Reminder: create virtual environment, it's always nice
```
python3 -m venv .venv
source .venv/bin/activate
```

## Requirements:

Install dependencies:
```
python3 -m pip install -r requirements.txt
```

Add env variables. Either create a `.env` file in this root directory, and add the GEOGUESSR_COOKIE:
```
GEOGUESSR_COOKIE="_ncfa={MY COOKIE VALUE}"
```
or export the value GEOGUESSR_COOKIE directly to your console:
```
export GEOGUESSR_COOKIE="_ncfa={MY COOKIE VALUE}"

```
The value for `{MY COOKIE VALUE}` can be found in the dev tools section of your browser. Look for the `_ncfa` value.

## Run the code:
Update the variable `challenge_id_list` in `main.py` with the correct list of Challenge IDs:
```Python
challenge_id_list = [
    "1234567890mnbvcxz",
    "1234567890mnbvcxz",
    "1234567890mnbvcxz",
    "1234567890mnbvcxz",
    "1234567890mnbvcxz",
    "1234567890mnbvcxz",
    "1234567890mnbvcxz",
    "1234567890mnbvcxz",
    "1234567890mnbvcxz",
    "1234567890mnbvcxz",
    ]  
```
And run the Python script:
```
python3 main.py
```
