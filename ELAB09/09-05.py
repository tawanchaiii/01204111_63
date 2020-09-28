import numpy as np
X = np.random.RandomState(1)
class Prince:
    def __init__(self,blood):
        self.blood = blood
        self.combo = -1
    def heal(self):
        self.blood+=20
        self.combo = -1
    def attack(self):
        self.combo += 1
        return (10 + self.combo*2)
    def damaged(self,d):
        self.blood-=d
        self.blood = max(0,self.blood)
    def showBlood(self):
        return max(self.blood,0)
class Monster:
    def __init__(self,blood):
        self.blood = blood
    def attack(self):
        return X.randint(1, 40)
    def damaged(self,d):
        self.blood-=d
        self.blood = max(0,self.blood)
    def showBlood(self):
        return max(self.blood,0)

b = int(input("Blood Start: "))
p1 = Prince(b)
m1 = Monster(b)
while (p1.showBlood() > 0 and m1.showBlood() > 0):
    op = input("Attack(a) or Heal(h): ")
    if op == 'a' : 
        m1.damaged(p1.attack())
        print(f"Monster's HP left {m1.showBlood()}")
    else :
        p1.heal()
        print(f"Your HP left {p1.showBlood()}")
    
    if m1.showBlood() == 0 : break
    
    p1.damaged(m1.attack())
    print(f"Monster's turn : Your HP left {p1.showBlood()}")

if p1.showBlood() == 0 :  print("You lose and die.(T_T)")
else : print("You win.(^_^)")