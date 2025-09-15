import pandas as pd
import csv
from datetime import datetime
from data_entry import get_montant, get_description, get_categorie, get_date


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "montant", "categorie", "description"]

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
