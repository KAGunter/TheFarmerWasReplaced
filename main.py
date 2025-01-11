while True:
	for i in range(get_world_size()):
		if(can_harvest()):
			harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Carrot)
		if(i < (get_world_size()-1)):
			move(North)
	
	move(North)
	move(East)
	
	for i in range(get_world_size()):
		if(can_harvest()):
			harvest()
			plant(Entities.Bush)
		if(i < (get_world_size()-1)):
			move(North)
	
	move(North)
	move(East)
	
	for i in range(get_world_size()):
		if(can_harvest()):
			harvest()
			plant(Entities.Bush)
		if(i < (get_world_size()-1)):
			move(North)
	
	move(North)
	move(East)
	
	for i in range(get_world_size()):
		if(can_harvest()):
			harvest()
		if(i < (get_world_size()-1)):
			move(North)
	
	move(North)
	move(East)
		