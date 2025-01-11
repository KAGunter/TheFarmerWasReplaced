def carrotPlant():
	if(can_harvest()):
		harvest()
	else:
		use_item(Items.Water)
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Carrot)
	