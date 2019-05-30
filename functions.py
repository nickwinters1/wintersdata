
#!/usr/bin/env python
"""
This file contains helper classes for working with DataFrames
"""
import numpy as np
import pandas as pd

class Cleaner:
    """
    The Cleaner Class is meant to provide a quick self cleaning of
    Python DataFrames
    """
    df = pd.DataFrame()

    def __init__(self, df):
        """
        Initialization of the Class, where it takes a DataFrame
        """
        self.df=df

    def dropna(self):
        """
        Drop NA values
        """
        self.df.dropna()

    def retdf(self):
        """
        Return the DF
        """
        return self.df

    def desc(self):
        """
        Describe the DF
        """
        return self.df.describe()
