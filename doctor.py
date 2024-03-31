# a class to collect data of doctor
class Account:
    def __init__(self, fname, lname, gender, birth, username, password):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.birth = birth
        self.username = username
        self.password = password

    def __str__(self):
        return "Bienvenu cher docteur. Le compte {} a ete cree avec succEs.".format(self.username)

# a class to create a register to manage doctors accounts
class RegisterDoctor:
    def __init__(self):
        self.registre = [] 

    def add_doctor(self, doc):
        self.register.append(doc)

    def display_doctor(self, doc):
        for elem in self.register:
            print(elem)
    
    def delete_doctor(self, doc):
        self.register.remove(doc)
    

class Consulting:
    def __init__(self, poids, tens_art, symptomes, antecedents, habitude_syst_corporels, remarques, prescription, prochain_rdv):
        self.poids = poids
        self.tens_art = tens_art
        self.symptomes = symptomes
        self.antecedents = antecedents
        self.habitude_syst_corporels = habitude_syst_corporels
        self.remarques = remarques
        self.prescription = prescription
        self.prochain_rdv = prochain_rdv