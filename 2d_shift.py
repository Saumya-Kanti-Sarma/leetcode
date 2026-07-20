"""
1260. Shift 2D Grid

You are given a 2D grid of size m x n and an integer k. Shift the grid k times.

In one shift operation:
    1. Element at grid[i][j] moves to grid[i][j + 1].
    2. Element at grid[i][n - 1] moves to grid[i + 1][0].
    3. Element at grid[m - 1][n - 1] moves to grid[0][0].

Return the 2D grid after applying the shift operation k times.


Example 1:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[9,1,2],[3,4,5],[6,7,8]]

    Explanation:
        The last element (9) moves to the first position.
        Every other element shifts one position to the right.

Example 2:
    Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

    Explanation:
        After four shifts, the last row becomes the first row.

Example 3:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    Output: [[1,2,3],[4,5,6],[7,8,9]]

    Explanation:
        The grid contains 9 elements.
        Shifting 9 times returns the grid to its original state.
"""

class Solution(object):
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        arr = []
        for row in grid:
            for num in row:
                arr.append(num)

        size = len(arr)
        k %= size

        result = [0] * size

        for i, num in enumerate(arr):
            new_index = (i + k) % size
            result[new_index] = num

        final_result = []
        idx = 0

        for i in range(m):
            row = []
            for j in range(n):
                row.append(result[idx])
                idx += 1
            final_result.append(row)

        return final_result