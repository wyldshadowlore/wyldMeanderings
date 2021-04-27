import random as r

class monster:
	def __init__(self, name, hp, attack, defense):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.defense = defense

enemies = [
('ogre', r.randrange(15 ,20 ,1), 10, 10),
('imp', r.randrange(2, 7, 1), 2, 1),
('wolf', r.randrange(5, 9, 1), 1, 4),
('lore spider', r.randrange(1, 25, 1), r.randrange(0, 10, 2), r.randrange(0, 10, 2)),
]