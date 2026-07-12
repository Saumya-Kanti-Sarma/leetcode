class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_unique = sorted(set(arr))
        rank_map = {}
        rank = 1
        for num in sorted_unique:
            rank_map[num] = rank
            rank += 1
        result = []
        for i in arr:
            result.append(rank_map[i])
        return result