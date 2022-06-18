import json

class FamilyNode:

    def __init__(self, name, genre, partner, childrens):
        self.name = name
        self.genre = genre
        self.partner = partner
        self.childrens = childrens
        
        self.facts = []

        if len(self.partner) == 0:
            self.hasPartner = False
        else:
            self.hasPartner = True

        if len(self.childrens) == 0:
            self.hasChildrens = False
        else:
            self.hasChildrens = True

        self.makeFacts()
    
    def makeFacts(self):
        if self.genre == 'F':
           self.facts.append(f'is_female("{self.name}").')

           if self.hasChildrens:
               self.facts += [f'is_mother("{self.name}","{x}").' for x in self.childrens]
 
        if self.genre == 'M':
           self.facts.append(f'is_male("{self.name}").')
           
           if self.hasChildrens:
               self.facts += [f'is_father("{self.name}","{x}").' for x in self.childrens]

        if self.hasPartner:
            self.facts.append(f'are_married("{self.name}","{self.partner}").')
            
            if self.genre == 'F':
                self.facts.append(f'is_male("{self.partner}").')
                self.facts += [f'is_father("{self.partner}","{x}").' for x in self.childrens]
            if self.genre == 'M':
                self.facts.append(f'is_female("{self.partner}").')
                self.facts += [f'is_mother("{self.partner}","{x}").' for x in self.childrens]
            self.facts.append(f'are_married("{self.partner}","{self.name}").')

    def printFacts(self):
       return '\n'.join(self.facts)

    def __str__(self):
        return 'name: ' + self.name + '\n' \
               'genre: ' + self.genre + '\n' \
               'partner: ' + self.partner + '\n' \
               'childs: ' + '\n' + '\n'.join(self.childrens)

def treeTraveler(familyObjList, familyleaf):

    familyObjList.append(
        FamilyNode(
            familyleaf['nombre'], 
            familyleaf['genero'] ,
            familyleaf['conyuge'], 
            [x['nombre'] for x in familyleaf['hijos']]
        )
    )
    for x in familyleaf['hijos']:
        treeTraveler(familyObjList, x) 
        

if __name__=='__main__':

    familyDict = {}
    with open("arbol_genealogico.json") as file:
        familyDict= json.load(file)

    familyObjList = []
    rulesSet = set()

    for x in familyDict:
        treeTraveler(familyObjList,x)
                        
    #print('\n'.join([x.printFacts() for x in familyObjList]))
    
    rulesList = []
    for x in familyObjList:
        rulesSet.update(x.facts)

    rules ={
        'is_male':[],
        'is_female':[],
        'is_father':[],
        'is_mother':[],
        'are_married':[]

        }

    for key in rules.keys():
        for rule in rulesSet: 
            if key in rule:
                rules[key].append(rule)
                print(rule)

    with open('facts.pl','w') as facts_file:
        for value in rules.values():
            for fact in value:
                facts_file.write(fact)
                facts_file.write('\n')
        
        
