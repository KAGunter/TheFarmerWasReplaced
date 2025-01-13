def hayPlant():
	if can_harvest():
		harvest()
	# cannot grow in Soil
	if get_ground_type() == Grounds.Soil:
		till()
	
	