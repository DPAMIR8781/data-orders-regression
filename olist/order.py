import pandas as pd
import numpy as np
from pathlib import Path


class Order:

    def __init__(self):
        self.data = self.get_data()

    def get_data(self):
        path = Path(__file__).resolve().parents[1] / "data"
        orders = pd.read_csv(path / "orders.csv")
        order_reviews = pd.read_csv(path / "order_reviews.csv")

        df = orders.merge(order_reviews, on="order_id", how="left")

        df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
        df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"])
        df["order_estimated_delivery_date"] = pd.to_datetime(df["order_estimated_delivery_date"])

        return df

    def get_training_data(self, with_distance_seller_customer=False):

        df = self.data.copy()

        df["wait_time"] = (
            df["order_delivered_customer_date"] - df["order_purchase_timestamp"]
        ).dt.days

        df["delay_vs_expected"] = (
            df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]
        ).dt.days

        df["delay_vs_expected"] = df["delay_vs_expected"].apply(lambda x: x if x > 0 else 0)

        df = df[[
            "order_id",
            "review_score",
            "wait_time",
            "delay_vs_expected"
        ]]

        df = df.dropna()

        return df
