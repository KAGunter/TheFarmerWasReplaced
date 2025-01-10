while True:
	for i in range(get_world_size()):
		harvest()
		if(i < (get_world_size()-1)):
			move(North)
		
	move(East)
	
	for i in range(3):
		harvest()
		if(i < (get_world_size()-1)):
			move(South)
		
	move(East)
	
	for i in range(get_world_size()):
		if(can_harvest()):
			harvest()
		if(i < (get_world_size()-1)):
			move(North)
		
	move(East)
	
	for i in range(3):
		do_a_flip()
		harvest()
		plant(Entities.Bush)
		if(i < (get_world_size()-1)):
			move(South)
			
	move(East)
		
	for i in range(get_world_size()):
		do_a_flip()
		harvest()
		plant(Entities.Bush)
		if(i < (get_world_size()-1)):
			move(North)
		
	move(East)
	for i in range(3):
		do_a_flip()
		plant(Entities.Bush)
		if(i < (get_world_size()-1)):
			move(South)
		
	move(East)