import pygame

pygame.init()

#TIME
FPS = 200
TIME_INC = 0.05

#SIZES
BALL_W = 10
BALL_H = 10

PATH_WIDTH = 2

BUTTON_WIDTH = 150
L_BUTTON_WIDTH = 350
BUTTON_HEIGHT = 50

CANNON_WIDTH = 100
CANNON_HEIGHT = 125

TEXT_BOX_WIDTH = 150
TEXT_BOX_HEIGHT = 50

#COLORS
D_GREEN = (57, 125, 15)
D_GREY = (81, 81, 81)
GREY = (128, 128, 128)
L_GREY = (175, 175, 175)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#OFFSETS
CANNON_OFFSET_X = 20

CONTROLLER_OFFSET_X = 100
CONTROLLER_OFFSET_Y = 700
CONTROLLER_BUTTON_OFFSET_X = 100

PROJECTILE_INIT_CANNON_OFFSET_Y = 60

CONTROLLER_OFFSET_MULTIPLIER_Y = 1.375

TEXTBOX_OFFSET_Y = 350
TEXTBOX_OFFSET_X = 200
TEXT_OFFSET = 12

LABEL_OFFSET_X = 175
LABEL_OFFSET_Y = 15

#INIT VALUES
INIT_ANGLE = 45

#FONTS
DEFAULT_F = pygame.font.SysFont('consolas', 20, True)