def mathTastic():
	
	# count actual number of items in inventory
	totalHay=num_items(Items.Hay)
	totalWood=num_items(Items.Wood)
	totalCarrots=num_items(Items.Carrot)
	generalDeficit=(totalDesired-(totalHay+totalWood+totalCarrots))
	
	# calculate how many of each crop should be in next round of planting
	hayNeed=round(((0.4*totalDesired-totalHay)/generalDeficit) * worldArea)
	woodNeed=round(((0.4*totalDesired-totalWood)/generalDeficit) * worldArea)
	carrotNeed=round(((0.2*totalDesired-totalCarrots)/generalDeficit) * worldArea)
	carrotNeed=(carrotNeed+(worldArea-(carrotNeed + woodNeed + hayNeed)))
	
	return hayNeed, woodNeed, carrotNeed
	
	
	
	