from datetime import datetime
date_format = "%Y-%m-%d"

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strftime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Format de date non valide. Veuillez saisir la date au format aaaa-mm-jj.")
        return get_date(prompt,allow_default)
    
def get_montant():
    pass

def get_categorie():
    pass

def get_description():
    pass

