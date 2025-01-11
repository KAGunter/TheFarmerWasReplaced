def normMovement():
	yPos=(get_pos_y())
	if(sideLength==yPos+1):
		move(East)
	move(North)
