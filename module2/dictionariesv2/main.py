# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        'name': name,
        'date_of_birth': date_of_birth,
        'place_of_birth': place_of_birth,
        'height': height,
        'nationality': nationality
    }
    return passport

def add_stamp(passport, country):
    if 'stamps' not in passport:
        passport["stamps"] = [country]
    else:
        if country not in passport['stamps']:
            passport['stamps'].append(country)
    return passport

def add_biometric_data(passport, name, value, date):
    if 'biometric' not in passport:
        passport['biometric'] = {name:{"date":date, "value":value}}
    else:
        passport['biometric'][name] = {"date":date, "value":value}
    return passport
    

#passport = create_passport('testname', '2000-01-01', 'place', '156,23', 'country')
#print(add_stamp(passport, 'stampcountry')) 

#if __name__ == "__main__":