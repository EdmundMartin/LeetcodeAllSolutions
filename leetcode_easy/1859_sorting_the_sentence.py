

class Solution:
    def sortSentence(self, s: str) -> str:
        split = s.split(' ')
        results = []
        for s in split:
            results.append((s[:-1], int(s[-1])))
        res = sorted(results, key=lambda x: x[1])
        return ' '.join([res[0] for res in res])