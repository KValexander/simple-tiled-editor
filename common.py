# Handling mouse collision
def mouseCollision(xy, wh, pos):
	if( xy[0] < pos[0] and (xy[0] + wh[0]) > pos[0]
		and xy[1] < pos[1] and (xy[1] + wh[1]) > pos[1]):
		return True
	else: return False