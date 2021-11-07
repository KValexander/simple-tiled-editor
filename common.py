# Handling mouse collision
def mouseCollision(xy, wh, pos):
	x, y = pos
	if( xy[0] < x and (xy[0] + wh[0]) > x
		and xy[1] < y and (xy[1] + wh[1]) > y):
		return True
	else: return False