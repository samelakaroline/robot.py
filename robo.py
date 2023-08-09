# -*- coding: utf8 -*-

import random

class position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '<%s, %s>' % (self.x, self.y)
    
class reward(position):
    def __init__(self, x, y, nome):
        super(reward, self).__init__(x, y)
        self.nome = nome
    def __str__(self):
        return '<%s, %s, %s>' % (self.x, self.y, self.name )
    def __repr__(self):
        return 'rewards %s' % str(self)
    
class robot(position):
    def up(self):
         if self.y < 10:
            self.y = self.y + 1
         else:
            print("O movimento é proibido!!")

    def down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print("O movimento é proibido !!")

    def left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print("O movimento é proibido !!")

    def right(self):
        if self.x < 10:
            self.x = self.x + 1
        else:
            print("O movimento é proibido !!")

def check_reward(robot, rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print("O robô encontrou a recompensa: %s" % reward.nome)
            ok = True
    return ok

r1 = reward(random.randint(0,10), random.randint(0,10), 'Ouro')
r2 = reward(random.randint(0,10), random.randint(0,10), 'Prata')
r3 = reward(random.randint(0,10), random.randint(0,10), 'Bronze')


Robo = robot(random.randint(0,10), random.randint(0,10))
rewards = [r1,r2,r3]

for e in range(10): 
     moviment = input ('Digite as posições do robô (up, down, right e left):')
     if moviment == 'up':
        Robo.up()
     elif moviment == 'down':
        Robo.down()
     elif moviment == 'right':
        Robo.right()
     elif moviment == 'left':
        Robo.left()
     else:
         print ('Movimento inválido!')
         continue
     print(Robo)
     check_reward(Robo,rewards )

