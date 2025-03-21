import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(1234567890)
random.seed(1234567890)

def excel_date_to_int(month, day, year):
    date = datetime(year, month, day)
    epoch = datetime(1899, 12, 30)
    delta = date - epoch
    return delta.days

def get_distribution(data, field):
    return data[field].value_counts().to_dict()

def weighted_random(items, weights):
    return random.choices(items, weights=weights, k=1)[0]

def create_named_storms_for_year():
    hurricane_names = ['Alex', 'Bill', 'Claudette', 'Danny', 'Elsa']
    cyclone_numbers = [f'Cyclone #{num}' for num in range(1, 4)]
    return {'Hurricane (Typhoon)': hurricane_names, 'Tropical Storm': cyclone_numbers}

def generate_random_date(weather_event, year):
    season = {'Hurricane (Typhoon)': (6, 11), 'Winter Storm': (11, 3)}.get(weather_event, (1, 12))
    start_month, end_month = season
    month = random.randint(1, 12)
    last_day = (datetime(year, month 