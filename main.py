#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author Philosophy Lee

from life_game import LifeGame
from matplotlib import pyplot as plt
from matplotlib import animation
import pysnooper

@pysnooper.snoop()
def show_animation(w = 48, h = 27, p = 0.5, i = 60):

    sl = LifeGame(h, w, p)

    fig = plt.figure()
    im = plt.imshow(sl.game_map.cells, animated=True,
                    cmap=plt.get_cmap("spring_r"), aspect="equal")

    def animate(*args):
        sl.game_cycle()
        im.set_array(sl.game_map.cells)
        return (im, )

    ani = animation.FuncAnimation(fig, animate, interval=60, blit=True)
    plt.show()


if __name__ == '__main__':
    # str_in = input("请输入相应的长、宽、初始生成的细胞的概率、图像的时间间隔(单位为ms)\n")
    # a, b, c, d = [eval(n) for n in str_in.split(" ")]  
    show_animation()
