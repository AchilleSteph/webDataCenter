class Account:
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd

    def __str__(self):
        return "Bienvenu cher utilisateur. Le compte {} a ete cree avec succEs.".format(self.username)

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