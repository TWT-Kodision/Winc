# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line


def alphabetical_order(list):
    list_sorted = sorted(list)
    return list_sorted

def won_golden_globe(film):
    winners=['Jaws'.lower(), 'Star Wars: Episode IV'.lower(), 'E.T. the Extra-Terrestrial'.lower(), 'Memoirs of a Geisha'.lower()]
    has_won = film.lower() in winners
    return has_won

def remove_toto_albums(list):
    toto_albums = ['Fahrenheit','The Seventh One','Toto XX', 'Falling in Between', 'Toto XIV','Old Is New']
    if (toto_albums[0] in list ):
        list.remove(toto_albums[0])
    if (toto_albums[1] in list ):
        list.remove(toto_albums[1])
    if (toto_albums[2] in list ):
        list.remove(toto_albums[2])
    if (toto_albums[3] in list ):
        list.remove(toto_albums[3])
    if (toto_albums[4] in list ):
        list.remove(toto_albums[4])
    if (toto_albums[5] in list ):
        list.remove(toto_albums[5])
    return list
