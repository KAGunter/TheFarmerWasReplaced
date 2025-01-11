def normMovement():
	yPos=(get_pos_y())
	move(North)
	if(sideLength==yPos+1):
		move(East)
	
