def treePlant():
	needsPlanting=1
	while (needsPlanting==1):
		xType = ((get_pos_x() + 1) % 2)
		yType = ((get_pos_y() + 1) % 2)
		if (xType != 0) and (yType != 0):
			if can_harvest():
				harvest()
				plant(Entities.Tree)
				use_item(Items.Water)
			needsPlanting=0
		elif((xType != 0) and (yType == 0)):
			normMovement()
		elif (xType == 0) and (yType != 0):
			normMovement()
		elif (xType == 0) and (yType == 0):
			if can_harvest():
				harvest()
				plant(Entities.Tree)
				use_item(Items.Water)
			needsPlanting=0