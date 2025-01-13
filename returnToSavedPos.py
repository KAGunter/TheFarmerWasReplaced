def returnToSavedPos(xSave, ySave):
	xCurrentPos=get_pos_x()
	yCurrentPos=get_pos_y()
	xDiff=xSave-xCurrentPos
	yDiff=ySave-yCurrentPos
	
	while xCurrentPos != xSave:
		if xDiff >= halfLength:
			move(West)
			xCurrentPos=get_pos_x()
		else:
			move(East)
			xCurrentPos=get_pos_x()
	while yCurrentPos != xSave:
		if xDiff >= halfLength:
			move(North)
			yCurrentPos=get_pos_y()
		else:
			move(South)
			yCurrentPos=get_pos_y()		