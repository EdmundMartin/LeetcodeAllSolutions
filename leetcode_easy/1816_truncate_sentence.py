

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        split_sentence = s.split(" ")
        if k == len(split_sentence):
            return s
        negative_idx = k - len(split_sentence)
        return ' '.join(split_sentence[:negative_idx])


if __name__ == '__main__':
    result = Solution().truncateSentence("Hello how are you Contestant", 4)
    print(result)