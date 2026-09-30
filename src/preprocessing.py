import pandas as pd


def clean_text(value):
    if pd.isna(value):
        return ""

    value = str(value).lower().strip()
    return " ".join(value.split())


def load_data(file_path):
    return pd.read_csv(file_path, sep="\t")


def preprocess_dataframe(df):
    df = df.copy()

    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].apply(clean_text)

    return df