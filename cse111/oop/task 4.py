
#task 4

class Joker:
    def __init__(self,name,power,psycho):
        self.name=name
        self.power=power
        self.is_he_psycho=psycho
        
j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print('=====================')
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print('=====================')
if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')

print("For first 'if', it is different because the memory location of j1 and j2 is different")
print("For the second 'if', it is same because right before the 'if' condition we changed the j2.name and renamed it like j1.name")
       