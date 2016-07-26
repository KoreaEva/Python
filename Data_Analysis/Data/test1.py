import json
from collections import Counter
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

path = 'ch02/usagov_bitly_data2012-03-16-1331923249-2.txt'
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

frame = DataFrame(records)

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    
    return counts

def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

counts = Counter(time_zones)

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] == 'Unknown'
tz_counts = clean_tz.value_counts()

print(tz_counts[:10])
tz_counts[:10].plot(kind='barh', rot=0)