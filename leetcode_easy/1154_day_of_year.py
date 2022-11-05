

class Solution:
    DAYS_OF_YEAR = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self, year: int):
        if year % 4 != 0:
            return False
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True

    def dayOfYear(self, date: str) -> int:

        year, month, day = date.split('-')

        total_days = 0
        for idx in range(int(month) - 1):
            total_days += self.DAYS_OF_YEAR[idx]
        total_days += int(day)

        if self.is_leap_year(int(year)):
            if int(month) > 2:
                total_days += 1

        return total_days


if __name__ == '__main__':
    res = Solution().dayOfYear("2019-01-09")
    print(res)