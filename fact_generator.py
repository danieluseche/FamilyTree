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

        if self.genre == 'M':
           self.facts.append(f'is_male("{self.name}").')   
        
        if self.hasChildrens:
            self.facts += [f'is_parent("{self.name}","{x}").' for x in self.childrens]

        if self.hasPartner:
            self.facts.append(f'are_married("{self.name}","{self.partner}").')
            
            if self.genre == 'F':
                self.facts.append(f'is_male("{self.partner}").')
                
            if self.genre == 'M':
                self.facts.append(f'is_female("{self.partner}").')

            self.facts += [f'is_parent("{self.partner}","{x}").' for x in self.childrens]
            self.facts.append(f'are_married("{self.partner}","{self.name}").')

    def printFacts(self):
       return '\n'.join(self.facts)

    def __str__(self):
        return 'name: ' + self.name + '\n' \
               'genre: ' + self.genre + '\n' \
               'partner: ' + self.partner + '\n' \
               'childs: ' + '\n' + '\n'.join(self.childrens)

def treeTraveler(familyObjList, familyleaf):
    #Falta mejor implementación de la recursión
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

    #Leer el arbol Genealogico del archivo JSON
    familyDict = {}
    with open("arbol_genealogico.json") as file:
        familyDict= json.load(file)

    #Lista de cada nodo del arbol para obtener sus hechos adecuados
    familyObjList = []
    #Itera entre ramas familiares sin relacion
    for x in familyDict:
        treeTraveler(familyObjList,x)
    
    #Se utiliza un set para evitar los hechos repetidos
    facts_Set = set()
    for x in familyObjList:
        facts_Set.update(x.facts)

    #lista de hechos posibles en un arbol genealogico
    facts_list =[
        'is_male',
        'is_female',
        'is_parent',
        'are_married'
        ]

    #Escribe en el archivo facts.pl los hechos organizadas por tipo
    with open('facts.pl','w') as facts_file:
        for key in facts_list:
            for fact in facts_Set: 
                if key in fact:
                    print(fact)
                    facts_file.write(fact)
                    facts_file.write('\n')