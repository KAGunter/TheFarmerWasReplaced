def mathTastic():
	
	# count actual number of items in inventory
	# prints deficit before every round of planting so it's easier to see when approaching goal
	totalHay=num_items(Items.Hay)
	totalWood=num_items(Items.Wood)
	totalCarrots=num_items(Items.Carrot)
	totalPumpkins=num_items(Items.Pumpkin)
	generalDeficit=(totalDesired-(totalHay+totalWood+totalCarrots+totalPumpkins))
	print(generalDeficit)
	
	# pumpkin plots allocated first
	pumpkinNeed= squarePlant()
	pumpkinlessWorldArea= worldArea - pumpkinNeed
	
	# calculate how many of each plot should be in next round of planting
	hayNeed=round(((0.5*totalDesired-totalHay)/generalDeficit) * pumpkinlessWorldArea)
	woodNeed=round(((0.2*totalDesired-totalWood)/generalDeficit) * pumpkinlessWorldArea)
	carrotNeed=round(((0.3*totalDesired-totalCarrots)/generalDeficit) * pumpkinlessWorldArea)
	#pumpkinNeed=round(((0.1*totalDesired-totalPumpkins)/generalDeficit) * worldArea)
	carrotNeed=(carrotNeed+(worldArea- (carrotNeed + woodNeed + hayNeed + pumpkinNeed)))
	
	return hayNeed, woodNeed, carrotNeed, pumpkinNeed
	
	
	
	