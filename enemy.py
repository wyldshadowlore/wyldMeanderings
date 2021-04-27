import random as r

class monster:
	def __init__(self, name, hp, attack, defense):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.defense = defense

enemies = [
('ogre', (15,20,1), (8,10,1), (8,10,1) ),
('imp', (2,7,1), (1,2,1), (1,2,1) ),
('wolf', (5,9,1), (1,2,1), (3,4,1) ),
('lore spider', (1,25,1), (1,11,2), (1,11,2) ),
]