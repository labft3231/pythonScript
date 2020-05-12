#!/usr/bin/env python
# coding: utf-8

import pandas as pd

def executionDF():
    s1 = pd.core.series.Series( [1, 2, 3, 4, 5] )
    s2 = pd.core.series.Series( ["one", "two", "three", "four", "five", "six", "seven"])
    df = pd.DataFrame(data=dict(num=s1, word=s2, a=''))
    return df.to_json(orient='records')

