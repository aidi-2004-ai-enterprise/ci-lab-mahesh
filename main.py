import pandas as pd
import seaborn as sns  # To load the penguin dataset easily

def load_penguin_data():
    """Load penguin dataset and return DataFrame shape"""
    df = sns.load_dataset("penguins")  # loads penguin dataset as DataFrame
    return df.shape

if __name__ == "__main__":
    shape = load_penguin_data()
    print(f"Penguin dataset shape: {shape}")