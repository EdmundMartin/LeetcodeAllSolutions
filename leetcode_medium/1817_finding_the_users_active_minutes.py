from typing import List
from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users_to_actions = defaultdict(set)
        for log in logs:
            users_to_actions[log[0]].add(log[1])

        uam_to_users = defaultdict(int)

        for val in users_to_actions.values():
            uam_to_users[len(val)] += 1
        result = []
        for i in range(k):
            if i + 1 in uam_to_users:
                result.append(uam_to_users[i+1])
            else:
                result.append(0)
        return result


if __name__ == '__main__':
    test_input = Solution().findingUsersActiveMinutes([[0,5],[1,2],[0,2],[0,5],[1,3]], 5)
    print(test_input)
