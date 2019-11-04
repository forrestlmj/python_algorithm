import sys


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        d = dict()
        l = [i for i in map(chr,range(97,97+25))]
        for i in licensePlate:
            if str.lower(i) not in l:
                continue
            elif str.lower(i) not in d:
                d[str.lower(i)] = 1
            else:
                d[str.lower(i)] += 1
        re = list()
        for word in words:
            w = d.copy()
            can = True
            for i in word:
                if i in w:
                    w[i] -= 1
            for i in w.values():
                if i > 0:
                    can = False
            if can:
                re.append(word)
        min_len = sys.maxsize
        min_word = None
        for w in re:
            if len(w) < min_len:
                min_len = len(w)
                min_word = w
        # print(min_word)
        return min_word
s = Solution()
s.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"])
s.shortestCompletingWord(licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"])
