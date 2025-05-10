import pandas as pd
import time
from utils.geoguessr import Geoguessr
from utils.util import clean
from utils.util import process_final_results

# initialize our instance of the class
geo = Geoguessr()

## List of Challenge IDs. All must be completed by your user BEFOREHAND, otherwise you cannot fetch the challenge results and the query will fail.
challenge_id_list = [
    "F9NDT5j10zorrtx3",
    "D2XcG4f6RPPYFjfI",
    "dJYyo33IcBLpSCqF",
    "s7ZmyQBMZ3IajIro",
    "dhxB1INIpdD2Rr2U",
    "EzSjAW17PV0avub6",
    "mCsYjIsSGUsmdFOL",
    "q6WYpeA3mQfWZo5N",
    "bQdbBzWNceHcq0K4",
    "7UkhiMmxUI5zXRUf",
    ]  

all_scores_df = []
# Collect dataframe with all the results
for challenge_id in challenge_id_list:
    # Query Geoguessr API to get the raw data
    raw_data = geo.get_challenge_scores(challenge_id)
    # Clean data and get Dataframe
    challenge_scores_df = clean(raw_data)
    # Concat results
    if type(all_scores_df) is list:
        all_scores_df = challenge_scores_df
    else: 
        all_scores_df = pd.concat([all_scores_df, challenge_scores_df])
    time.sleep(0.1) ## to not overwhelm the API

# Final processing
final_results = process_final_results(all_scores_df)
print(final_results)

