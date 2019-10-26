# https://leetcode.com/problems/bulls-and-cows/
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        a_count, b_count, g_dict,b_set = 0, 0, dict(),set()
        secret = list(secret)
        guess = list(guess)
        i = 0
        while i < len(secret):
            if secret[i] == guess[i]:
                secret.remove(secret[i])
                guess.remove(guess[i])
                a_count += 1
            else:
                i+=1


        for i in range(len(guess)):
            if guess[i] not in g_dict.keys():
                g_dict[guess[i]] = 1
            else:
                g_dict[guess[i]] += 1
        for i in range(len(secret)):
            if secret[i] in g_dict.keys():
                b_count += 1
                if g_dict[secret[i]] == 1:
                    g_dict.pop(secret[i])
                else:
                    g_dict[secret[i]] -= 1
        return str(a_count)+"A"+str(b_count)+"B"


def test():
    s = Solution()
    assert s.getHint( secret = "1", guess = "1") == "1A0B"
    assert s.getHint( secret = "1", guess = "2") == "0A0B"
    assert s.getHint( secret = "11111", guess = "11111") == "5A0B"
    assert s.getHint( secret = "11112", guess = "11211") == "3A2B"

    assert s.getHint( secret = "1807", guess = "7810") == "1A3B"
    assert s.getHint( secret = "1123", guess = "0111") == "1A1B"
def test1():
    s = Solution()
    assert s.getHint( secret = "1122", guess = "2211") == "0A4B"
def test2():
    s = Solution()
    assert s.getHint( secret = "11", guess = "10") == "1A0B"
def test3():
    s = Solution()

    assert s.getHint( secret = "11122", guess = "22311") == "0A4B"

if __name__ == "__main__":
    test()
    test1()
    test2()
    test3()