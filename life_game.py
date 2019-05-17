# -*- coding: utf-8 -*-
#
# @author Philosophy Lee

from game_map import GameMap


class LifeGame(object):

    def __init__(self, map_rows=10, map_cols=10, life_init_possibility=0.5):
        self.game_map = GameMap(map_rows, map_cols)
        self.game_map.reset(life_init_possibility)

    def game_cycle(self):
        nc_map = self.game_map.get_neighbor_count_map()
        for row in range(self.game_map.rows):
            for col in range(self.game_map.cols):
                nc = nc_map[row][col]
                if nc < 2 or nc > 3:
                    self.game_map.set(row, col, 0)
                elif nc == 3:
                    self.game_map.set(row, col, 1)
