# Flood Fill
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
#
# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from
# the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting
# pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with
# the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.
#
# Return the modified image after performing the flood fill.
#
# Example 1: Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2 Output: [[2,2,2],[2,2,0],[2,0,
# 1]] Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels
# connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
#
# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
# Output: [[2,2,2],[2,2,2]]
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image

        def fill(a: List[List[int]], i: int, j: int):
            if (0 > i or i >= len(a)) or (0 > j or j >= len(a[i])) or a[i][j] != color:
                return

            a[i][j] = newColor

            # up
            fill(a, i - 1, j)
            # down
            fill(a, i + 1, j)
            # left
            fill(a, i, j - 1)
            # right
            fill(a, i, j + 1)

        fill(image, sr, sc)
        return image


if __name__ == '__main__':
    res = Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
    print(res)

    res = Solution().floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1)
    print(res)
