import requests
import streamlit as st
import json
import pandas as pd
import numpy as np

response = requests.get("https://api.atlasfreeshard.com/news/all")

json = response.json()

keys = list(json[0].keys())

for key in json:
    if key == 'realm' and 'realm' == 'Albion':
        print('Alb')
    else:
        print('not alb')

