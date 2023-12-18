import pandas as pd

FILL_VALUES = {'mean': lambda x: x.mean(), 
               'median': lambda x: x.median(),
               'mode': lambda x: x.mode()[0]}

class Imputer:

    def __init__(self, fill_strategy='mean'):
        self.fill_func = FILL_VALUES[fill_strategy]
        
    def fit_transform(self, df, columns):
        df = df.copy()
        for col in columns:
            fill_value = self.fill_func(df[col]) 
            df[col].fillna(fill_value, inplace=True)
        return df
        
data = {'A': [1, 2, None, 4], 'B': [5, None, 7, 8]} 
df = pd.DataFrame(data)

imputer = Imputer(fill_strategy='median')
df_imputed = imputer.fit_transform(df, df.columns)
print(df_imputed)