import pandas as pd
import csv
from datetime import datetime
from data_entry import get_montant, get_description, get_categorie, get_date


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "montant", "categorie", "description"]
    FORMAT = "%Y-%m-%d"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, montant, categorie, description):
        new_entry = dict(
            date=date, montant=montant, categorie=categorie, description=description
        )
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Donées ajoutées avec succès")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strftime(start_date, CSV.FORMAT)
        end_date = datetime.strftime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)

        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("Aucune transaction trouvée dans la plage des dates données")
        else:
            print("OK")




def add():
    CSV.initialize_csv()

    date = get_date(
        "Entrez la date de la transaction (aaaa-mm-jj) Ou tapez entré pour la date d'aujourd'hui : ",
        allow_default=True,
    )
    montant = get_montant()
    categorie = get_categorie()
    description = get_description()

    CSV.add_entry(date, montant, categorie, description)

add()
