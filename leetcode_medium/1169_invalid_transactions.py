from typing import List
from collections import defaultdict



class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        cities = defaultdict(lambda: defaultdict(list))
        result = []

        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            cities[city][name].append(int(time))

        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time = int(time)
            if int(amount) > 1_000:
                result.append(transaction)
                continue

            for key, val in cities.items():
                if key == city:
                    continue

                if any([abs(x - time) <= 60 for x in val[name]]):
                    result.append(transaction)
                    break
        return result


if __name__ == '__main__':
    transactions = ["alice,20,800,mtv", "alice,50,100,beijing"]

    result = Solution().invalidTransactions(transactions)
    print(result)