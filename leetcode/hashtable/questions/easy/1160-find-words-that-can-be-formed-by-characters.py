# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int

        """
        ch_chars,l = dict(),0
        for i in chars:
            if i not in ch_chars.keys():
                ch_chars[i] = 1
            else:
                ch_chars[i] += 1
        for word in words:
            w_dict = ch_chars.copy()
            can_be_formed = True
            for w in word:
                if w not in w_dict.keys():
                    can_be_formed = False
                    break
                else:
                    w_dict[w] -= 1
                    if w_dict[w] < 0:
                        can_be_formed = False
                        break
            if can_be_formed:
                l += len(word)
        return l

def test():
    """

    :return:
    """
    s = Solution()
    assert s.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach") == 6
    assert s.countCharacters(words = ["caat","bt","hat","tree"], chars = "atch") == 3

    assert s.countCharacters( words = ["hello","world","leetcode"], chars = "welldonehoneyr") == 10
    # assert s.countCharacters( s = "a", t = "aa") == "a"
    # assert s.findTheDifference( s = "sdfse", t = "sedfss") == "s"
    #
    # assert s.getHint( secret = "1807", guess = "7810") == "1A3B"
    # assert s.getHint( secret = "1123", guess = "0111") == "1A1B"
# def test1():
#     s = Solution()
#     assert s.getHint( secret = "1122", guess = "2211") == "0A4B"
# def test2():
#     s = Solution()
#     assert s.getHint( secret = "11", guess = "10") == "1A0B"
# def test3():
#     s = Solution()
#
#     assert s.getHint( secret = "11122", guess = "22311") == "0A4B"

if __name__ == "__main__":
    test()
    # test1()
    # test2()
    # test3()