print("Welcome  to my computer quiz!")
print('\n')

playing = input("Do you want to play?  ")
print('\n')

if playing.lower() != 'yes':
    quit()

print('Okay! Let\'s play :) ')
score = 0

answer = input('What does CPU stand for? ')

if answer.lower() == 'central processing unit':
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect! ")
print('\n')

answer = input('What does RAM stand for? ')
if answer.lower() == 'random access memory':
    print("your answer is correct")
    score += 1
else:
    print("Your answer is incorrect! ")
print('\n')

answer = input('What does PSU stand for? ')
if answer.lower() == 'power supply':
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect! ")

print('\n')
print("Congratulations, you got " + str(round((score/3)*100, 2)) + " %." )
