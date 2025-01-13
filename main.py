# resets all plots + drone when code is restarted
clear()

# goal number of produce items
totalDesired=20000
numPumpkinPlots=1

sideLength = get_world_size()
halfLength = sideLength/2
worldArea = sideLength * sideLength
dronePositionSavedX= 0
dronePositionSavedY= 0


while True:
	
	# math out the ratios for balanced growth
	plantHay, plantWood, plantCarrots, plantPumpkin = mathTastic()
	
	
	# actually do planting
	for i in range(numPumpkinPlots):
		pumpkinPlant()
		
		
	for i in range(plantWood):
		returnOrigin()
		treePlant()
		normMovement()
		
		
	for i in range(plantHay):
		hayPlant()
		normMovement()

	for i in range(numPumpkinPlots):
		dronePositionSavedX, dronePositionSavedY = getDronePos()
		pumpkinPlant()
		returnToSavedPos(dronePositionSavedX, dronePositionSavedY)
	
	
	for i in range(plantCarrots):
		carrotPlant()
		normMovement()
	
