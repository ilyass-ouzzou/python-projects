import random
def draw_simulation(group:list):
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


pot1 = ['Qatar', 'Brazil', 'Belgium', 'France', 'Argentina', 'England', 'Spain' , 'Portugal']
pot2 = ['Mexico', 'Netherlands', 'Denmark', 'Germany', 'Uruguay', 'Switzerland', 'United States', 'Croatia']
pot3 = ['Senegal', 'Iran', 'Japan', 'Morocco', 'Serbia', 'Poland', 'South Korea', 'Tunisia']
pot4 = ['Cameroon', 'Canada', 'Ecuador', 'Saudi Arabia', 'Ghana', 'UEFA', 'AFC/CONMEBOL', 'CONCACAF/OFC']

groupA = []
print(draw_simulation(groupA))
groupB = []
print(draw_simulation(groupB))
groupC = []
print(draw_simulation(groupC))
groupD = []
print(draw_simulation(groupD))
groupE = []
print(draw_simulation(groupE))
groupF = []
print(draw_simulation(groupF))
groupG = []
print(draw_simulation(groupG))
groupH = []
print(draw_simulation(groupH))