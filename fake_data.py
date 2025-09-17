from faker import Faker
from datetime import datetime
import random
import csv

FORMAT = "%Y-%m-%d"
COLUMNS = ["date", "montant", "categorie", "description"]
# Initialisation du faker générateur
fake = Faker("fr_FR")

# Catégories possibles
categories = [
    "Alimentation",
    "Transport",
    "Logement",
    "Diverstissement",
    "Santé",
    "Shopping",
    "Abonnement",
    "Voyage",
]

# Générer une transaction aléatoire


def random_transaction():
    transactions = dict(
        date=fake.date_between(start_date="-1y", end_date="today").strftime(FORMAT),
        montant=round(random.uniform(5.0, 500), 2),
        categorie=random.choice(categories),
        description=fake.sentence(nb_words=6),
    )
    return transactions


# Insertion des données dans mon csv:
with open("finance_data.csv", "a", newline="") as csvfile:
    writer = csv.DictWriter(
        csvfile, fieldnames= COLUMNS
    )
    for i in range(500):
        writer.writerow(random_transaction())
    print("Données ajoutés avec succès")


