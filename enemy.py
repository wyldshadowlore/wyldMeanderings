import random as r

class monster:
	def __init__(self, name, hp, attack, defense, gold, experience, agility):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.gold = gold
		self.experience = experience
		self.agility = agility

enemies = [
('ogre', (15,20,1), (8,10,1), (8,10,1), 100, 10, 5 ),
('imp', (2,7,1), (1,2,1), (1,2,1), 5, 1, 11 ),
('wolf', (5,9,1), (1,2,1), (3,4,1), 0, 22, 45 ),
('lore spider', (1,25,1), (1,11,2), (1,11,2), 12, 14, 21 ),
]