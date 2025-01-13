def returnOrigin():
	xPos=get_pos_x()
	yPos=get_pos_y()
	while xPos != 0:
		move(West)
		xPos-= 1
	while yPos != 0:
		move(South)
		yPos-= 1