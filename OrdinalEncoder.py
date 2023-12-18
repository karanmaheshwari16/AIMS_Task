import pandas as pd

class OrdinalEncoder:
    def __init__(self, df, categorical_columns):
        self.df = df
        self.columns = categorical_columns
        self.mapping = {}
        
    def fit(self):
        for col in self.columns:
            self.mapping[col] = {cat: idx for idx, cat in enumerate(sorted(self.df[col].unique()))} 
        return self
    
    def transform(self):
        df_encoded = self.df.copy()
        for col, mapping in self.mapping.items():
            df_encoded[col] = df_encoded[col].map(mapping)
        return df_encoded
    
if __name__ == '__main__':
    data = {"Color": ["Red", "Blue", "Green", "Red"], 
            "Size": ["Big", "Small", "Medium", "Medium"]}
    
    df = pd.DataFrame(data)
    
    encoder = OrdinalEncoder(df, ["Color", "Size"])
    encoder.fit()
    df_encoded = encoder.transform()
    print(df_encoded)