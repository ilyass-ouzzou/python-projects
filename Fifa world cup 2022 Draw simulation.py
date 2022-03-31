import random
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
print("Group A : {}".format(draw_simulation(groupA)))
groupB = []
print("Group B : {}".format(draw_simulation(groupB)))
groupC = []
print("Group C : {}".format(draw_simulation(groupC)))
groupD = []
print("Group D : {}".format(draw_simulation(groupD)))
groupE = []
print("Group E : {}".format(draw_simulation(groupE)))
groupF = []
print("Group F : {}".format(draw_simulation(groupF)))
groupG = []
print("Group G : {}".format(draw_simulation(groupG)))
groupH = []
print("Group H : {}".format(draw_simulation(groupH)))


"""  
Output:

Group A : ['Qatar', 'Mexico', 'Iran', 'Saudi Arabia']
Group B : ['Portugal', 'Switzerland', 'Serbia', 'UEFA']
Group C : ['Spain', 'Croatia', 'Poland', 'Ghana']
Group D : ['Belgium', 'Uruguay', 'South Korea', 'CONCACAF/OFC']
Group E : ['Argentina', 'Netherlands', 'Tunisia', 'AFC/CONMEBOL']
Group F : ['France', 'United States', 'Japan', 'Ecuador']
Group G : ['Brazil', 'Germany', 'Morocco', 'Cameroon']         :( sad for Moroccans :(
Group H : ['England', 'Denmark', 'Senegal', 'Canada']

"""
