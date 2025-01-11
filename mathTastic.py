def mathTastic():
	
	# count actual number of items in inventory
	# prints deficit before every round of planting so it's easier to see when approaching goal
	totalHay=num_items(Items.Hay)
	totalWood=num_items(Items.Wood)
	totalCarrots=num_items(Items.Carrot)
	generalDeficit=(totalDesired-(totalHay+totalWood+totalCarrots))
	print(generalDeficit)
	
	# calculate how many of each crop should be in next round of planting
	hayNeed=round(((0.5*totalDesired-totalHay)/generalDeficit) * worldArea)
	woodNeed=round(((0.2*totalDesired-totalWood)/generalDeficit) * worldArea)
	carrotNeed=round(((0.3*totalDesired-totalCarrots)/generalDeficit) * worldArea)
	carrotNeed=(carrotNeed+(worldArea-(carrotNeed + woodNeed + hayNeed)))
	
	return hayNeed, woodNeed, carrotNeed
	
	
	
	