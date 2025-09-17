import pandas as pd
import matplotlib.pyplot as plt
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
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)

        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("Aucune transaction trouvée dans la plage des dates données")
        else:
            print(
                f"Transaction de {start_date.strftime(CSV.FORMAT)} à {end_date.strftime(CSV.FORMAT)}"
            )
            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}
                )
            )

            total_income = filtered_df[filtered_df["categorie"] == "Revenus"][
                "montant"
            ].sum()
            total_expense = filtered_df[filtered_df["categorie"] == "Dépenses"][
                "montant"
            ].sum()

            print("\nRésumé:")
            print(f"Revenu total : €{total_income:.2f}")
            print(f"Dépenses total : €{total_expense:.2f}")
            print(f"Économies nettes : €{(total_income - total_expense):.2f}")

        return filtered_df


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


def plot_transactions(df):
    df.set_index("date", inplace=True)
    income_df = (
        df[df["categorie"] == "Revenus"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    expense_df = (
        df[df["categorie"] == "Dépenses"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["montant"], label="Revenus", color="g")
    plt.plot(expense_df.index, expense_df["montant"], label="Dépenses", color="r")
    plt.xlabel("Date")
    plt.ylabel("Montant")
    plt.title("Revenus et dépenses au fil du temps")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\n 1. Ajouter une nouvelle transactions ")
        print(" 2. Afficher les transactions et leur résumé sur une période donnée ")
        print(" 3.Sortie")

        choice = input("Entrez votre choix (1-3) : ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Entrez la date de début au format (aaaa-mm-jj) : ")
            end_date = get_date(
                "Entrez la date de fin au format (aaaa-mm-jj) ou tapez entré pour la date d'aujourd'hui : ",
                allow_default=True,
            )
            df = CSV.get_transactions(start_date, end_date)
            if input("Voulez vous voir le graphique (y/n): ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Sortie...")
            break
        else:
            print("Choix invalide. Saisissez 1, 2 ou 3.")


if __name__ == "__main__":
    main()
