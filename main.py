clear()

sideLength = get_world_size()

while True:
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