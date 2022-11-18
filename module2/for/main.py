from importlib.machinery import WindowsRegistryFinder
from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
def shortest_length(countries):
    smallest_number = len(countries[0])
    for country in countries:
        if len(country) < smallest_number:
            smallest_number = len(country)
    return smallest_number

def add_to_list(existing_list, item):
    existing_list.append(item)
    return existing_list

def shortest_names(list_countries):
    smallest_number = shortest_length(list_countries)
    new_list_countries =[]
    for country in list_countries:
        if len(country) == smallest_number:
            new_list_countries = add_to_list(new_list_countries, country)
    return new_list_countries 
#=======================================================================================
def count_vowels(word):
    vowels =['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in range(len(word)):
        for vowel in vowels:
            if word[letter].lower() == vowel:
                count += 1
    return count

def find_most_vowels(list_words):
    most_vowels = 0
    for word in list_words:
        if count_vowels(word) > most_vowels:
            most_vowels = count_vowels(word)
            word_most_vowels = word
    return word_most_vowels

def most_vowels(list_words):
    top_three = []
    new_list = list_words
    for x in range(3): 
        word = find_most_vowels(new_list)
        #print(f'{x+1}. {word}')
        top_three.append(word)
        new_list.remove(word)
    return top_three
#============================================================================================

def make_alphabet():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return alphabet

def add_word_to_list(wordlist, word):
    wordlist.append(word)
    return wordlist

def remove_letter_from_list(letterlist, letter):
    if letter in letterlist: 
        letterlist.remove(letter)
    return letterlist

def count_similar_letters (letterlist, word):
    counter = 0
    for letter in word:
        for other_letter in letterlist:
            if letter == other_letter:
                counter += 1 
    return counter

def find_word_most_similar_letters(letterlist, wordlist):
    most_letters = 0
    selected_word = ""
    for word in wordlist:
        if count_similar_letters(letterlist, word.lower())>most_letters:
            selected_word = word
    return selected_word

def alphabet_set (wordlist):
    alphabet_list = []
    alphabet = make_alphabet()
    for x in range(len(wordlist)):
        selected_word = find_word_most_similar_letters(alphabet, wordlist)
        add_word_to_list(alphabet_list, selected_word)
        for letter in selected_word.lower():
            alphabet = remove_letter_from_list(alphabet, letter)
        if len(alphabet) == 0:
            break
    return alphabet_list


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    #print(shortest_names(countries))
    #make_top_three_most_vowels(countries)
    alphabet_set(countries)
    most_vowels(countries)
    

    """ Write the calls to your functions here. """
