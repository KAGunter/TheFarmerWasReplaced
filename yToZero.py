def yToZero():
	yPos=get_pos_y()
	while yPos !=0:
		move(South)
		yPos=get_pos_y()