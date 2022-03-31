import random
from colorama import Fore, Back, Style

def draw_simulation(group:list):
    if(group == groupA):
        pass
    else:
        from_pot1 = random.choice(pot1)
        group.append(from_pot1)
        pot1.remove(from_pot1)
    from_pot2 = random.choice(pot2)
    group.append(from_pot2)
    pot2.remove(from_pot2)
    from_pot3 = random.choice(pot3)
    group.append(from_pot3)
    pot3.remove(from_pot3)
    from_pot4 = random.choice(pot4)
    group.append(from_pot4)
    pot4.remove(from_pot4)
    return group


pot1 = ['Brazil', 'Belgium', 'France', 'Argentina', 'England', 'Spain' , 'Portugal'] # Qatar is in the first Group by default
pot2 = ['Mexico', 'Netherlands', 'Denmark', 'Germany', 'Uruguay', 'Switzerland', 'United States', 'Croatia']
pot3 = ['Senegal', 'Iran', 'Japan', 'Morocco', 'Serbia', 'Poland', 'South Korea', 'Tunisia']
pot4 = ['Cameroon', 'Canada', 'Ecuador', 'Saudi Arabia', 'Ghana', 'UEFA', 'AFC/CONMEBOL', 'CONCACAF/OFC']

groupA = []
groupA.append('Qatar')
print(Fore.BLUE + "Group A : {}".format(draw_simulation(groupA)))
groupB = []
print(Fore.RED + "Group B : {}".format(draw_simulation(groupB)))
groupC = []
print(Fore.YELLOW + "Group C : {}".format(draw_simulation(groupC)))
groupD = []
print(Fore.CYAN + "Group D : {}".format(draw_simulation(groupD)))
groupE = []
print(Fore.GREEN + "Group E : {}".format(draw_simulation(groupE)))
groupF = []
print(Fore.MAGENTA + "Group F : {}".format(draw_simulation(groupF)))
groupG = []
print(Fore.LIGHTYELLOW_EX + "Group G : {}".format(draw_simulation(groupG)))
groupH = []
print(Fore.LIGHTGREEN_EX + "Group H : {}".format(draw_simulation(groupH)))


"""

Group A : ['Qatar', 'Denmark', 'South Korea', 'Saudi Arabia']
Group B : ['France', 'United States', 'Serbia', 'Ghana']
Group C : ['Portugal', 'Netherlands', 'Tunisia', 'CONCACAF/OFC']
Group D : ['Argentina', 'Germany', 'Japan', 'AFC/CONMEBOL']
Group E : ['Spain', 'Uruguay', 'Morocco', 'UEFA']
Group F : ['Belgium', 'Mexico', 'Iran', 'Canada']
Group G : ['England', 'Switzerland', 'Senegal', 'Ecuador']
Group H : ['Brazil', 'Croatia', 'Poland', 'Cameroon']


"""
