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

        self.makeFacts();
    
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
            self.facts.append('\n')
            if self.genre == 'F':
                self.facts.append(f'is_male("{self.partner}").')
                self.facts += [f'is_father("{self.partner}","{x}").' for x in self.childrens]
            if self.genre == 'M':
                self.facts.append(f'is_female("{self.partner}").')
                self.facts += [f'is_mother("{self.partner}","{x}").' for x in self.childrens]
            self.facts.append(f'are_married("{self.partner}",{self.name}").')
            self.facts.append('\n')
        else:
            self.facts.append('\n')

    def printFacts(self):
       return '\n'.join(self.facts)

    def __str__(self):
        return 'name: ' + self.name + '\n' \
               'genre: ' + self.genre + '\n' \
               'partner: ' + self.partner + '\n' \
               'childs: ' + '\n' + '\n'.join(self.childrens)

if __name__=='__main__':
    familyDict = {}
    with open("arbol_genealogico.json") as file:
        familyDict= json.load(file)

    familyObjList = []
    familyObjList.append(
                FamilyNode(
                familyDict['nombre'],
                familyDict['genero'],
                familyDict['conyuge'],
                [x['nombre'] for x in familyDict['hijos']]))

    for sons in familyDict['hijos']:
        familyObjList.append(
        FamilyNode(
        sons['nombre'],
        sons['genero'],
        sons['conyuge'],
        [x['nombre'] for x in sons['hijos']]))

        for grandsons in sons['hijos']:
            familyObjList.append(
            FamilyNode(
            grandsons['nombre'],
            grandsons['genero'],
            grandsons['conyuge'],
            [x['nombre'] for x in grandsons['hijos']]))
                        
    print('\n'.join([x.printFacts() for x in familyObjList]))
