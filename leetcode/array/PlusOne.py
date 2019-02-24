class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits) -1

        while (index >= 0):
            if digits[index] == 9:
                digits[index] =0
                # 第一位是9
                if index == 0:
                    digits.insert(0, 0)
                else:
                    index -= 1
            else:
                digits[index] += 1
                return digits


def test_0():
    s = Solution()

    digits = [1,9,1,3,9,9]
    assert s.plusOne(digits) == [1,9,1,4,0,0]
    digits = [1,2,3]
    assert s.plusOne(digits) == [1,2,4]
    digits = [4,3,2,1]
    assert s.plusOne(digits) == [4,3,2,2]
    digits = [0]
    assert s.plusOne(digits) == [1]
    digits = [9]
    assert s.plusOne(digits) == [1,0]
    digits = [9,9]
    assert s.plusOne(digits) == [1,0,0]
    digits = [9,0,9,0]
    assert s.plusOne(digits) == [9,0,9,1]
    digits = [9,3,9,9]
    assert s.plusOne(digits) == [9,4,0,0]
if __name__ == "__main__":
    test_0()
