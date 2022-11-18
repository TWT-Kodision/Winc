from operator import truediv
from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

def set_max(number):
    if number> 1000:
        number=1000
        return number
    else:
        return number

def register_fact(list_of_facts, fact):
    list_of_facts.append(fact)
    return list_of_facts

def facts_in_list(list_of_facts, fact):
    if fact in list_of_facts:
        return True
    else:
        return False

def unique_koala_facts(number):
    number = set_max(number)
    max_iteration = 1000
    list_of_facts = []
    while max_iteration > 0:
        if number > 0:
            fact = random_koala_fact()
            if (facts_in_list(list_of_facts, fact)) == False:
                list_of_facts = register_fact(list_of_facts, fact)
                #print(number)
                number -= 1
        max_iteration -= 1        
    return list_of_facts

#==========================================================


def list_count_fact(list_of_facts, fact):
    number = list_of_facts.count(fact)
    return number

def is_particular_fact_ten_times(list_of_facts):
    max_number = 10
    times_fact = 0
    is_ten_times = False
    for fact in list_of_facts:
        if (list_count_fact(list_of_facts, fact))> times_fact:
            times_fact = list_count_fact(list_of_facts, fact)
        if times_fact == max_number:
            is_ten_times = True
            break
    return is_ten_times

def make_particular_fact_list():
    fact_list =[]
    while is_particular_fact_ten_times(fact_list) == False:
        fact_list = register_fact(fact_list, random_koala_fact())
    return fact_list

def contain_word_joey(fact):
    contain_joey = False
    if "joey" in fact.lower():
        contain_joey = True
    return contain_joey

def make_unique_joeys_facts_list(list_of_facts):
    unique_joey_facts_list = []
    for fact in list_of_facts:
        if contain_word_joey(fact) and (fact in unique_joey_facts_list) == False:
                register_fact(unique_joey_facts_list, fact)
    return unique_joey_facts_list

def num_joey_facts():
    joey_fact_list = make_unique_joeys_facts_list(make_particular_fact_list())
    print(joey_fact_list)
    number = len(joey_fact_list)
    return number
    
#===================================================================
def is_weigh_in_string(string):
    weigh_in_string = False
    if "weigh" in string.lower() and "kg" in string.lower():
        weigh_in_string = True
    return weigh_in_string

def find_fact_with_weigh():
    fact = ""
    while is_weigh_in_string(fact)== False:
            fact = random_koala_fact()
    return fact

def find_kg(string):
    index = string.index("kg")
    weight = string[index-2:index]
    print(weight)
    return weight

def koala_weight():
    weight_fact = find_fact_with_weigh()
    weight = find_kg(weight_fact)
    return int(weight)




# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    #print(random_koala_fact())
    #print(make_particular_fact_list())
    #print(list_count_fact(test_facts, fact))
