while True:
	if can_harvest():
		harvest()
	move(North)
	if can_harvest():
		harvest()
	move(North)
	if can_harvest():
		harvest()
	move(South)
	if can_harvest():
		harvest()
	move(South)
