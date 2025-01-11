def hayPlant():
	if can_harvest():
		harvest()
	if get_ground_type() == Grounds.Soil:
		till()
	
	