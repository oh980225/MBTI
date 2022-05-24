import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

MBTI = pd.read_csv('input/MBTI 500.csv')

plt.figure(figsize=(12,5))
plt.plot(MBTI['type'].value_counts())
plt.title('Distribution of Classes')
plt.show()