def pumpkinPlant():
	returnOrigin()
	pknSide=round(halfLength)+1
	if checkGreatPumpkin(pknSide):
		harvest()
	for j in range(pknSide):
		for k in range(pknSide):
			if can_harvest()==False:
				use_item(Items.Water)
			if (get_ground_type() == Grounds.Grassland):
					till()
			plant(Entities.Pumpkin)
			if k < pknSide-1:
				move(North)
		yToZero()
		if j < pknSide-1:
			move(East)