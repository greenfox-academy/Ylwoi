__author__ = 'ylwoi'

from tkinter import *


class Map(object):
    def __init__(self):
        self.tileX = 36
        self.tileY = 36
        self.floor_pic = PhotoImage(file='assets\Floor.png')
        self.wall_pic = PhotoImage(file='assets\wall.png')
        self.wall_matrix = [
            [3, 5], [3, 5, 7, 8], [1, 2, 3, 5, 7, 8], [5], [0, 1, 2, 3, 5, 6, 7, 8],
            [1, 3, 8], [1, 3, 5, 6, 8], [5, 6, 8], [1, 2, 3, 8], [3, 5, 6, 8], [1, 3, 5]
        ]

    def draw_floor(self, canvas):
        for draw_row in range(10):
            for draw_column in range(11):
                canvas.create_image(self.tileX+draw_row*72, self.tileY+draw_column*72, image=self.floor_pic)

    def draw_wall(self, canvas):
        for i in self.wall_matrix:
            for j in i:
               canvas.create_image(self.tileX + j*72, self.tileY + self.wall_matrix.index(i)*72, image=self.wall_pic)


class Hero(object):
    def __init__(self):
        self.heroX = 36
        self.heroY = 36
        self.hero_pic_down = PhotoImage(file='assets\hero-down.png')
        self.hero_pic_up = PhotoImage(file='assets\hero-up.png')
        self.hero_pic_left = PhotoImage(file='assets\hero-left.png')
        self.hero_pic_right = PhotoImage(file='assets\hero-right.png')

    def draw_hero(self, canvas, hero_picture):
        self.a = canvas.create_image(self.heroX, self.heroY, image=hero_picture)


class Skeleton(object):
    def __init__(self, x, y):
        self.skeleton_pic = PhotoImage(file='assets\skeleton.png')
        self.skeletonX = x
        self.skeletonY = y

    def draw_skeleton(self, canvas):
        self.ds = canvas.create_image(self.skeletonX, self.skeletonY, image=self.skeleton_pic)


class GameLogic(object):
    def __init__(self):
        canvas.bind("<KeyPress>", self.on_key_press)

    def move_control(self, x=0, y=0):
        self.hero_cord_x = (hero.heroX+x) // 72
        self.hero_cord_y = (hero.heroY+y) // 72
        if self.hero_cord_x < 0 or self.hero_cord_x > 9:
            return False
        if self.hero_cord_y < 0 or self.hero_cord_y > 10:
            return False
        for i in game_map.wall_matrix:
            for j in i:
                if self.hero_cord_x == j and self.hero_cord_y == game_map.wall_matrix.index(i):
                    return False
        return True

    def on_key_press(self, e):
        self.e = e
        canvas.delete(hero.a)
        if self.e.keysym == 'Up':
            if logic.move_control(0,-72) == True:
                hero.heroY = hero.heroY - 72
                hero.draw_hero(canvas, hero.hero_pic_up)
            else:
                hero.draw_hero(canvas, hero.hero_pic_up)

        elif self.e.keysym == 'Down':
            if logic.move_control(0,72) == True:
                hero.heroY = hero.heroY + 72
                hero.draw_hero(canvas, hero.hero_pic_down)
            else:
                hero.draw_hero(canvas, hero.hero_pic_down)

        elif self.e.keysym == 'Left':
            if logic.move_control(-72, 0) == True:
                hero.heroX = hero.heroX - 72
                hero.draw_hero(canvas, hero.hero_pic_left)
            else:
                hero.draw_hero(canvas, hero.hero_pic_left)

        elif self.e.keysym == 'Right':
            if logic.move_control(72,0) == True:
                hero.heroX = hero.heroX + 72
                hero.draw_hero(canvas, hero.hero_pic_right)
            else:
                hero.draw_hero(canvas, hero.hero_pic_right)


root = Tk()
canvas = Canvas(root, width=720, height=792)

game_map = Map()
hero = Hero()
logic = GameLogic()
skel_1 = Skeleton(108,36 )

canvas.pack()
canvas.focus_set()

game_map.draw_floor(canvas)
game_map.draw_wall(canvas)
hero.draw_hero(canvas, hero.hero_pic_down)
skel_1.draw_skeleton(canvas)

root.mainloop()

