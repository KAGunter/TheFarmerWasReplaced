def checkGreatPumpkin(checkSideLength):
	totalNeeded=checkSideLength*checkSideLength
	grPumpkHarvest=False
	punkinCount=0
	for j in range(checkSideLength):
		for k in range(checkSideLength):
			if (get_entity_type()==Entities.Pumpkin) and (can_harvest()):
				punkinCount+=1
			move(North)
		yToZero()
		move(East)
	
	if punkinCount==totalNeeded:
		grPumpkHarvest=True
	returnOrigin()
		
	return grPumpkHarvest