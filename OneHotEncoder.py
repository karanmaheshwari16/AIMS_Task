import pandas as pd
import numpy as np

class OneHotEncoder:
    def __init__(self, df, columns):
        self.columns = columns
        self.df = df
        
    def startEncode(self):
        unique_vals = {}
        for col in self.columns:
            unique_vals[col] = self.df[col].unique()
            
        for col in unique_vals.keys():
            for val in unique_vals[col]:
                self.df[val] = 0
                
        for i, row in self.df.iterrows():
            for col in self.columns:
                self.df.at[i, row[col]] = 1
                
        self.df = self.df.drop(self.columns, axis=1)
        self.df = self.df.dropna(axis=1)
        
        return self.df
                
if __name__ == '__main__':

    data = {'color': ['red', 'blue', 'green', 'red'], 
            'size': ['S', 'M', 'L', 'M']}
    df = pd.DataFrame(data)
    
    ohe_cols = ['color', 'size']
    
    encoder = OneHotEncoder(df, ohe_cols)
    encoded_df = encoder.startEncode()
    
    print(encoded_df)