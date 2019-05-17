# -*- coding: utf-8 -*-
#
# @author Philosophy Lee

import numpy as np


class GameMap(object):
    """
    游戏地图包含很多单元格。
    每个单元格都有一个值，0表示它是一个空/空单元格，1表示它是一个活动单元格。
    属性:大小
    """

    MAX_MAP_SIZE = 2000
    MAX_CELL_VALUE = 1
    DIRECTIONS = (
        (0, 1, ),
        (0, -1, ),
        (1, 0, ),
        (-1, 0, ),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    )
    '''这个元组用来计算边角处的邻居数目'''
    def __init__(self, rows, cols):
        """用行和列计数初始化游戏地图。"""
        if not isinstance(rows, int):
            raise TypeError("行需要是整数")
        if not isinstance(cols, int):
            raise TypeError("列需要是整数")
        assert 0 < rows <= self.MAX_MAP_SIZE
        assert 0 < cols <= self.MAX_MAP_SIZE
        self.size = (rows, cols, )
        self.cells = np.zeros((rows, cols), dtype = int)
        
    @property
    def rows(self):
        """初始化行数"""
        return self.size[0]

    @property
    def cols(self):
        """初始化列数"""
        return self.size[1]

    def reset(self, possibility=0.5):
        """随机进行初始化地图"""
        assert 0 < possibility < 1
        self.cells = np.random.randint(0, 2, size=(self.rows, self.cols))

    def get(self, row, col):
        """获取地图中的特定单元格。"""
        if not isinstance(row, int):
            raise TypeError("行需要是整数")
        if not isinstance(col, int):
            raise TypeError("列需要是整数")
        assert 0 <= row < self.rows
        assert 0 <= col < self.cols
        return self.cells[row][col]

    def set(self, row, col, val):
        """获取地图中的特定单元格。"""
        if not isinstance(row, int):
            raise TypeError("行需要是整数")
        if not isinstance(col, int):
            raise TypeError("列需要是整数")
        if not isinstance(val, int):
            raise TypeError("值需要是整数")
        assert 0 <= row < self.rows
        assert 0 <= col < self.cols
        assert 0 <= val <= self.MAX_CELL_VALUE
        self.cells[row][col] = val
        return self

    def get_neighbor_count(self, row, col):
        """计算某个特定单元格的邻居数

        Args:
            row: 行号
            col: 列号

        Returns:
            Count of live neighbor cells
            邻居的细胞个数
        """
        if not isinstance(row, int):
            raise TypeError("行需要是整数")
        if not isinstance(col, int):
            raise TypeError("列需要是整数")
        assert 0 <= row < self.rows
        assert 0 <= col < self.cols
        count = 0
        for d in self.DIRECTIONS:
            d_row = row + d[0]
            d_col = col + d[1]
            if d_row >= self.rows:
                d_row -= self.rows
            if d_col >= self.cols:
                d_col -= self.cols
            count += self.cells[d_row][d_col]
        return count

    def get_neighbor_count_map(self):
        return [
        [self.get_neighbor_count(row, col) for col in range(self.cols)]
        for row in range(self.rows)
        ]

    def set_map(self, new_map):
        self.cells = new_map
