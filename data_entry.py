from datetime import datetime

date_format = "%Y-%m-%d"
CATEGORIES = {"R": "Revenus", "D": "Dépenses"}


def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strftime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print(
            "Format de date non valide. Veuillez saisir la date au format aaaa-mm-jj."
        )
        return get_date(prompt, allow_default)


def get_montant():
    try:
        montant = float(input("Entrez le montant: "))
        if montant <= 0:
            raise ValueError(
                "Le montant doit être une valeur non négative et différente de zéro"
            )
        return montant
    except ValueError as e:
        print(e)
        return get_montant()


def get_categorie():
    categorie = input(
        "Entrez la catégorie ('R' pour les revenus ou 'D' pour les dépenses): "
    ).upper()
    if categorie in CATEGORIES:
        return CATEGORIES[categorie]

    print("Catégorie non valide. Veuillez saisir 'R' ou 'D': ")
    return get_categorie


def get_description():
    return input("Entrez une description (facultatif) : ")
