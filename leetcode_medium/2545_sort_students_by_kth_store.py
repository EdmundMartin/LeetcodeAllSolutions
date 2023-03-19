from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
       return sorted(score, key=lambda x: x[k], reverse=True)


if __name__ == '__main__':
    test = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]

    result = Solution().sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2)
    print(result)