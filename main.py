import pygame
pygame.init()


W, H = 600, 720
FPS = 30
GRAY = (35, 35, 35)
operation = ''
last_key = ''
res = '0'
operand = '0'
number = '0'

flag_bip = 1

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Calculator from Vados')

bg_surf = pygame.image.load('images/calc.jpg')
f = pygame.font.Font('font.ttf', 112)

clock = pygame.time.Clock()
def check_len():
	if len(number.replace(' ','')) < 8:
		return 1
	else: return 0

def input_d(digit):
	global number, last_key, flag_bip
	if check():
		if check_len():
			number += digit
	else:
		number = digit
	last_key = digit
	flag_bip = 0

def summ(slog1, slog2):
	if '.' in slog1 or '.' in slog2:
		return str(float(slog1.replace(' ', '')) + float(slog2.replace(' ', '')))
	else: return str(int(slog1.replace(' ', '')) + int(slog2.replace(' ', '')))

def check():
	if last_key in ['+'] or number == '0':
		return 0
	else:
		return 1

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif event.type == pygame.KEYDOWN:
			if event.key in [pygame.K_BACKSPACE, pygame.K_DELETE]:
				if last_key not in ['+']:	
					if number[-1] == '1':
						number = number[:-2]
					else:	
						number = number[:-1]
				if len(number) == 0:
					number = '0'
				flag_bip = 0
			elif event.key in [pygame.K_KP0, pygame.K_0]:
				input_d('0')
			elif event.key in [pygame.K_KP1, pygame.K_1]:
				input_d('1')
			elif event.key in [pygame.K_KP2, pygame.K_2]:
				input_d('2')
			elif event.key in [pygame.K_KP3, pygame.K_3]:
				input_d('3')
			elif event.key in [pygame.K_KP4, pygame.K_4]:
				input_d('4')
			elif event.key in [pygame.K_KP5, pygame.K_5]:
				input_d('5')
			elif event.key in [pygame.K_KP6, pygame.K_6]:
				input_d('6')
			elif event.key in [pygame.K_KP7, pygame.K_7]:
				input_d('7')
			elif event.key in [pygame.K_KP8, pygame.K_8]:
				input_d('8')
			elif event.key in [pygame.K_KP9, pygame.K_9]:
				input_d('9')
			elif event.key in [pygame.K_KP_PERIOD, pygame.K_PERIOD]:
				if '.' not in number:
					input_d('.')
			elif event.key == pygame.K_KP_PLUS:
				if res == '0':
					res = number.replace(' ', '')
					operand = number
				elif last_key == '+':
					res = summ(res, operand)
				else:
					res = summ(res, number)
					operand = number
				if res[-2:] == '.0':
					res = res[:-2]
				number = res.replace('1', ' 1')
				operation = '+'
				last_key = '+'
				flag_bip = 0
			elif event.key in [pygame.K_KP_ENTER, pygame.K_EQUALS]:
				if operand != '0':
					if operation == '+':
						print(operand, res)
						res = summ(operand, number)
						number = res
				number = res.replace('1', ' 1')
				flag_bip = 0
				print(res, operand, operation, number)

	digit = f.render(number, 1, GRAY)
	digit_pos = digit.get_rect(bottomright =(540, 220))

	sc.blit(bg_surf, (0, 0))
	if flag_bip:
		sc.blit(digit, digit_pos)
	else: flag_bip = 1
	pygame.display.update()

	clock.tick(FPS)