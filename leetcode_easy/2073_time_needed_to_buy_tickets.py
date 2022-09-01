from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = [(idx, t) for idx, t in enumerate(tickets)]

        count = 0
        while tickets:
            count += 1
            leader_idx, leader = tickets[0]
            if leader - 1 == 0:
                if leader_idx == k:
                    return count
                else:
                    tickets = tickets[1:]
            else:
                tickets = tickets[1:]
                tickets.append((leader_idx, leader - 1))