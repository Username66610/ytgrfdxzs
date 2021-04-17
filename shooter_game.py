'''
#Создай собственный Шутер!
lost = 0
from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
    
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 420:
            self.rect.x += self.speed

    def fire(self):
        buiiet = Buiiet('Bullet.png',self.rect_x,0,15)
        bullets.add(bullet)

class Enemy(GameSprite):
    direction = 'down'
    def update(self):
        if self.rect.y < 500:
            self.rect.y +=self.speed
            global lost
        else:
            self.rect.x = randint(5,635)
            self.rect.y = 0
            lost = lost + 1     

class Buiiet(GameSprite):
    def update(self):
        self.rect_x -= self.speed
        if self.rect_y < 0:
            self.kill()



win_width = 700
win_height = 500
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("ЪуЪ космос")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
game = True
clock = time.Clock()
FPS = 60 
hero = Player('rocket.png', 300, 400, 10)
bullets = sprite.Group()

ufo = Enemy("ufo.png",randint(5,635),0,randint(1,2) )
ufo2 = Enemy("ufo.png",randint(5,635),0,randint(1,2) )
ufo3 = Enemy("ufo.png",randint(5,635),0,randint(1,2) )
ufo4 = Enemy("ufo.png",randint(5,635),0,randint(1,2) )
ufo5 = Enemy("ufo.png",randint(5,635),0,randint(1,2) )
font.init()
font = font.Font(None, 70)
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

window = display.set_mode((win_width, win_height))
bullets = sprite.Group()
Ufo_group = sprite.Group()
Ufo_group.add(ufo)
Ufo_group.add(ufo2)
Ufo_group.add(ufo3)
Ufo_group.add(ufo4)
Ufo_group.add(ufo5)
score = 0 
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()

    

    window.blit(background,(0,0))
 
    hero.update()
    hero.reset()
    ufo.update()
    bullets.update()

    collides = sprite.groupcollide(Ufo_group,bullets,True,True)

    for c in collides:
        score += 1
        ufo = Enemy("ufo.png",randint(80,620),0,randint(1,5))
        ufo.add(ufo)

    if sprite.spritecollide(hero,Ufo_group,False) or lost>=3:
        game = False

    if score >= 10:
        game = False
    display.update()
'''
from pygame import *
from random import randint
#подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.Font('Arial', 80)
win = font1.render('ЕСТЬ -10 ЙУ-ХУ', True, (255, 255, 255))
lose = font1.render('ФУУбот', True, (180, 0, 0))
 
font2 = font.Font('Arial', 36)
 
#фоновая музыка
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
 
#нам нужны такие картинки:
img_back = "galaxy.jpg" #фон игры
img_bullet = "bullet.png" #пуля
img_hero = "rocket.png" #герой
img_enemy = "ufo.png" #враг
score = 0 #сбито кораблей
goal = 10 #столько кораблей нужно сбить для победы
lost = 0 #пропущено кораблей
max_lost = 10 #проиграли, если пропустили столько
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
 
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
 #метод "выстрел" (используем место игрока, чтобы создать там пулю)
   def fire(self):
       bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
       bullets.add(bullet)
 
#класс спрайта-врага  
class Enemy(GameSprite):
   #движение врага
   def update(self):
       self.rect.y += self.speed
       global lost
       #исчезает, если дойдёт до края экрана
       if self.rect.y > win_height:
           self.rect.x = randint(80, win_width - 80)
           self.rect.y = 0
           lost = lost + 1
#класс спрайта-пули  
class Bullet(GameSprite):
   # движение врага
   def update(self):
       self.rect.y += self.speed
       # исчезает, если дойдет до края экрана
       if self.rect.y < 0:
           self.kill()
#создаём окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
#создаём спрайты
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
#создание группы спрайтов-врагов
monsters = sprite.Group()
for i in range(1, 6):
   monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 1))
   monsters.add(monster)
bullets = sprite.Group()
#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку Закрыть
   for e in event.get():
       if e.type == QUIT:
           run = False
       #событие нажатия на пробел - спрайт стреляет
       elif e.type == KEYDOWN:
           if e.key == K_SPACE:
               fire_sound.play()
               ship.fire()
 #сама игра: действия спрайтов, проверка правил игры, перерисовка
   if not finish:
       #обновляем фон
       window.blit(background,(0,0))
 
       #производим движения спрайтов
       ship.update()
       monsters.update()
       bullets.update()
 
       #обновляем их в новом местоположении при каждой итерации цикла
       ship.reset()
       monsters.draw(window)
       bullets.draw(window)
       #проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают)
       collides = sprite.groupcollide(monsters, bullets, True, True)
       for c in collides:
           #этот цикл повторится столько раз, сколько монстров подбито
           score = score + 1
           monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 1))
           monsters.add(monster)

       #возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
       if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
           finish = True #проиграли, ставим фон и больше не управляем спрайтами.
           window.blit(lose, (200, 200))
 
       #проверка выигрыша: сколько очков набрали?
       if score >= goal:
           finish = True
           window.blit(win, (200, 200))
 
       #пишем текст на экране
       text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
       window.blit(text, (10, 20))
 
       text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
       window.blit(text_lose, (10, 50))
 
       display.update()