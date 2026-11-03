
import pandas as pd

class Univariate:

    def quanQual(self, dataset):
        qual = []
        quan = []

        for columnName in dataset.columns:
            if pd.api.types.is_string_dtype(dataset[columnName].dtype):
                qual.append(columnName)
            else:
                quan.append(columnName)

        return quan, qual
