import pandas as pd


def calculate_metrics(df):
    df = df.copy()

    df["CTR"] = (df["cliques"] / df["impressoes"]) * 100
    df["CPC"] = df["investimento"] / df["cliques"]
    df["CPM"] = (df["investimento"] / df["impressoes"]) * 1000
    df["CPA"] = df["investimento"] / df["conversoes"]
    df["Taxa_Conversao"] = (df["conversoes"] / df["cliques"]) * 100
    df["ROAS"] = df["receita"] / df["investimento"]

    df["CTR"] = df["CTR"].round(2)
    df["CPC"] = df["CPC"].round(2)
    df["CPM"] = df["CPM"].round(2)
    df["CPA"] = df["CPA"].round(2)
    df["Taxa_Conversao"] = df["Taxa_Conversao"].round(2)
    df["ROAS"] = df["ROAS"].round(2)

    return df