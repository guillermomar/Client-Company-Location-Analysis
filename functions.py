import re
import pandas as pd
import math


def money(money):
    match = re.search(r"(\d+(\.)*(\d+)*)(\w*)",money)
    if match:
        return float(match.group(1))

def units(money):
    match = re.search(r"(\d+(\.)*(\d+)*)(\w*)",money)
    if match:
        return match.group(4)

def change_colour(val):
    return ['background-color: red' if x < 370  else 'background-color: green' for x in val]

def geo_Json(lat,lng):
    try:
        lat = float(lat)
        lng = float(lng)
        
        if not math.isnan(lat) and not math.isnan(lng):
            return {
                "type":"Point",
                "coordinates":[lng,lat]
            }
    except Exception:
        return None


#companies_df_clean["location"] = companies_df_clean[["latitude", "longitude"]].apply(lambda x: geo_Json(x.latitude,x.longitude), axis=1)


