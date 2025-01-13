def pumpkinPlant():
	returnOrigin()
	pknSide=round(sideLength/2)
	if checkGreatPumpkin(pknSide):
		harvest()
	for j in range(pknSide):
		for k in range(pknSide):
			if can_harvest()==False:
				use_item(Items.Water)
			if (get_ground_type() == Grounds.Grassland):
					till()
			plant(Entities.Pumpkin)
			move(North)
		yToZero()
		move(East)