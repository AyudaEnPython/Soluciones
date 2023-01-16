"""
Shooting Game
=============

You are creating a shooting game!
The game has two types of enemies, aliens and monsters. You shoot the
aliens using your laser, and monsters using your gun.

Each hit decreases the lives of the enemies by 1.

The given code declares a generic Enemy class, as well as the Alien and
Monster classes, with their corresponding lives count.
It also defines the hit() method for the Enemy class.

You need to do the following to complete the program:
1. Inherit the Alien and Monster classes from the Enemy class.
2. Complete the while loop that continuously takes the weapon of choice
    from user input and call the corresponding object's hit() method.

Sample input:
laser
laser
gun
exit

Sample Output:
Alien has 4 lives
Alien has 3 lives
Monster has 2 lives

Hint:
The while loop stops when the user enters 'exit'.
"""


class Enemy:
    name = ""
    lives = 0

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            print(self.name + ' killed')
        else:
            print(self.name + ' has '+ str(self.lives) + ' lives')


class Monster(Enemy):

    def __init__(self):
        super().__init__('Monster', 3)


class Alien(Enemy):

    def __init__(self):
        super().__init__('Alien', 5)


m = Monster()
a = Alien()

while True:
    x = input()
    if x == 'exit':
        break
    if x == 'laser':
        a.hit()
    if x == 'gun':
        m.hit()

# while True:
#     x = input()
#     if x == 'exit':
#         break
#     a.hit() if x == 'laser' else m.hit()
