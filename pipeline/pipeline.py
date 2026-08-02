import sys
from datetime import datetime
import pandas as pd  # type: ignore[import-not-found]

print('arguments', sys.argv)

month = int(sys.argv[1]) if len(sys.argv) > 1 else datetime.now().month

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df['month'] = month
print(df.head())

print(f'hello pipeline, month={month}')

