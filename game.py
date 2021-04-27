import enemy as e
import random as r


def callMon():
	selectmon = r.choice(e.enemies)
	mon = e.monster(selectmon[0],r.randrange(*selectmon[1]),r.randrange(*selectmon[2]),r.randrange(*selectmon[3]))

	print(mon.name, mon.hp, mon.attack, mon.defense)

callMon()