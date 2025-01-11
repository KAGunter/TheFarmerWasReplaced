def bushPlant():
	if(can_harvest()):
		harvest()
	else:
		use_item(Items.Water)
	plant(Entities.Bush)