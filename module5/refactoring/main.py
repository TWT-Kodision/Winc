__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


class HomeOwner():
    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = [needs]
        self.contracts = []
    
    def addNeed(self, new_need):
        self.needs.append(new_need)

    def removeNeed(self, rm_need):
        self.needs.remove(rm_need)
    
    def contract(self, specialist):
        for need in self.needs:
            if specialist.speciality == need:
                self.contracts.append(specialist.name)

        

class Specialist():
    def __init__(self, name, speciality, price):
        self.name = name
        self.speciality = speciality
        self.price = price

Alfred = HomeOwner ("Alfred", "Alfredslane 123","painter")
print (Alfred.needs)
Alfred.addNeed("plumber")
print(Alfred.needs)
alice = Specialist("alice", "electrian", 12)
bob = Specialist("bob", "painter", 12)
craig = Specialist("craig", "painter", 12)
Alfred.contract(alice)
Alfred.contract(bob)
Alfred.contract(craig)
print(Alfred.contracts)


'''

""""
class Electrician(Specialist):
    def specialist(self):
        self.speciality = "electrician"
        
class Painter(Specialist):
    def specialist(self):
        self.speciality = "painter"

class Plumber(Specialist):
    def specialist(self):
        self.speciality = "plumber"

class ListSpecialists():
    list = []
    def add_specialist(self, name):
        list.append(name)
    
    def remove_specialist(self, name):
        list.remove(name)

"""



alice_name = "Alice Aliceville"
alice_profession = "electrician"
bob_name = "Bob Bobsville"
bob_profession = "painter"
craig_name = "Craig Craigsville"
craig_profession = "plumber"

alfred_name = "Alfred Alfredson"
alfred_address = "Alfredslane 123"
alfred_needs = ["painter", "plumber"]
bert_name = "Bert Bertson"
bert_address = "Bertslane 231"
bert_needs = ["plumber"]
candice_name = "Candice Candicedottir"
candice_address = "Candicelane 312"
candice_needs = ["electrician", "painter"]

alfred_contracts = []
for need in alfred_needs:
    if need == alice_profession:
        alfred_contracts.append(alice_name)
    elif need == bob_profession:
        alfred_contracts.append(bob_name)
    elif need == craig_profession:
        alfred_contracts.append(craig_name)

bert_contracts = []
for need in bert_needs:
    if need == alice_profession:
        bert_contracts.append(alice_name)
    elif need == bob_profession:
        bert_contracts.append(bob_name)
    elif need == craig_profession:
        bert_contracts.append(craig_name)

candice_contracts = []
for need in candice_needs:
    if need == alice_profession:
        candice_contracts.append(alice_name)
    elif need == bob_profession:
        candice_contracts.append(bob_name)
    elif need == craig_profession:
        candice_contracts.append(craig_name)

print("Alfred's contracts:", alfred_contracts)
print("Bert's contracts:", bert_contracts)
print("Candice's contracts:", candice_contracts)
'''