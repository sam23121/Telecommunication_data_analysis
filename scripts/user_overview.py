import pandas as pd
import numpy as np

class OverViewAnalysis:
    
    def __init__(self, df):
        
        self.df = df

    def top_handset_type(self, top=10):
        
        return self.df['handset_type'].value_counts().head(top)
    
    def top_manufacturer(self, top=3):
        
        return self.df['handset_manufacturer'].value_counts().head(top)
    
    def top_handset_by_manufacturer(self, manufacturer, top=5):
        
        return self.df.groupby('handset_manufacturer')['handset_type'].value_counts()[manufacturer].head(top)