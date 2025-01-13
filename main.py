# resets all plots + drone when code is restarted
clear()

# goal number of produce items
totalDesired=20000

sideLength = get_world_size()
worldArea = sideLength * sideLength


while True:
	
	# math out the ratios for balanced growth
	plantHay, plantWood, plantCarrots = mathTastic()
	
	
	
	for i in range(plantWood):
		treePlant()
		normMovement()
		
		
	for i in range(plantHay):
		hayPlant()
		normMovement()
	
	
	for i in range(plantCarrots):
		carrotPlant()
		normMovement()
	
