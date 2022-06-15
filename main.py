from operator import contains
import requests
import streamlit as st
import json
import pandas as pd
import numpy as np

response = requests.get("https://api.atlasfreeshard.com/news/all")

json = response.json()

st.table(json)

midgard = 0
albion = 0
hibernia = 0

for i in json:
    statline = i.values()
    if 'RvR' in statline:
        if 'Midgard' in statline:
            midgard+= 1
        elif 'Hibernia' in statline:
            hibernia+= 1
        elif 'Albion' in statline:
            albion+= 1
print(midgard)
print(hibernia)
print(albion)

keeps = pd.Series([midgard,hibernia,albion])

st.bar_chart(keeps)