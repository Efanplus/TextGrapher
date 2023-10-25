import pandas as pd
import numpy as np
from text_grapher import *
data = pd.read_csv("recall_result.csv", sep='\t')
data = data["texts"]
content = data[0]
handler = CrimeMining()
print("content", content)
handler.main(content)