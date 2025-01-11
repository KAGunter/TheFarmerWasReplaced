# resets all when code is restarted
clear()

# goal number of produce items
totalDesired=10000

sideLength = get_world_size()
worldArea = sideLength * sideLength


while True:
	
	plantHay, plantWood, plantCarrots = mathTastic()
	
	
	for i in range(sideLength):
		harvest()
		if(can_harvest()):
			harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Carrot)

		normMovement()
	
	for i in range(get_world_size()):
		if(can_harvest()):
			harvest()
			plant(Entities.Bush)
		normMovement()
	
	for i in range(get_world_size()):
		if(can_harvest()):
			harvest()
			plant(Entities.Bush)
		normMovement()
	
	for i in range(get_world_size()):
		if(can_harvest()):
			harvest()
		normMovement()