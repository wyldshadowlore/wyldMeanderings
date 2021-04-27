import enemy as e
import random as r

selectmon = r.choice(e.enemies)
mon = e.monster(selectmon[0],selectmon[1],selectmon[2],selectmon[3])

for i in range(1, 10, 1):
	selectmon = r.choice(e.enemies)
	mon = e.monster(selectmon[0],selectmon[1],selectmon[2],selectmon[3])

	print(mon.name, mon.hp, mon.attack, mon.defense)
