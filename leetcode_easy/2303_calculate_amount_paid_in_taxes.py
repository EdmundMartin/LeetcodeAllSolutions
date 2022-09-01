from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax_total = 0
        lower_band = 0
        for idx, bracket in enumerate(brackets):
            upper_band, rate = bracket
            if income < lower_band:
                return tax_total
            tax_band = min(upper_band, income)
            current_total = ((tax_band - lower_band) / 100) * rate
            tax_total += current_total
            lower_band = upper_band
        return tax_total


if __name__ == '__main__':
    result = Solution().calculateTax([[3,50],[7,10],[12,25]], 10)
    print(result)