# Import libraries
import pygame

# Handling mouse collision
def mouseCollision(xy, wh, pos):
	if( xy[0] < pos[0] and (xy[0] + wh[0]) > pos[0]
		and xy[1] < pos[1] and (xy[1] + wh[1]) > pos[1]):
		return True
	else: return False

# Handling border collision
def borderCollision(xy, wh, pos, border):
	if(
		(xy[0] < pos[0] and (xy[0] + wh[0]) > pos[0]
		and xy[1] < pos[1] and (xy[1] + wh[1]) > pos[1])
		and not
		(xy[0] + border < pos[0] and (xy[0] + wh[0]) - border * 2 > pos[0]
		and xy[1] + border < pos[1] and (xy[1] + wh[1]) - border * 2 > pos[1])
		):
		return True
	else: return False

# Load image
def loadImage(src):
	image = pygame.image.load(src)
	return image

# Scalable load image
def scLoadImage(src, size):
	image = pygame.image.load(src)
	image = pygame.transform.scale(image, size)
	return image

# Rendering load image
def drawImage(screen, image, xy):
	screen.blit(image, xy)

# Unscalable image
def unImage(screen, src, xy):
	image = pygame.image.load(src)
	screen.blit(image, xy)

# Scalable image
def scImage(screen, src, xy, size):
	image = pygame.image.load(src)
	image = pygame.transform.scale(image, size)
	screen.blit(image, xy)