# resets all plots + drone when code is restarted
clear()

# goal number of produce items
totalDesired=10000

sideLength = get_world_size()
worldArea = sideLength * sideLength


while True:
	
	# math out the ratios for balanced growth
	plantHay, plantWood, plantCarrots = mathTastic()
	
	
	for i in range(plantHay):
		if can_harvest():
			harvest()
		normMovement()
	
	for i in range(plantWood):
		bushPlant()
		normMovement()
	
	for i in range(plantCarrots):
		carrotPlant()
		normMovement()
	
