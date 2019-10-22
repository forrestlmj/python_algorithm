class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.

        """
        # for p2 in range(n):
        #     for p1 in range(m):
        #         if nums2[p2]>nums1[p1]:
        #             nums1.insert(p1+1,nums2[p2])
        #
        m_c = m
        n_c = n
        if n == 0 or len(nums2) == 0:
            # nums1 = nums1[:m]
            for i in range(len(nums1) - (m)):
                nums1.pop()
        elif m == 0 :
            nums1.clear()
            for i in nums2:
                nums1.append(i)
        else:
            p1, p2 = 0, 0
            while p1 < m and p2 < len(nums2):
                if nums2[p2] > nums1[p1]:
                    p1 += 1
                # nums1.insert(p1, nums2[p2])
                else:
                    nums1.insert(p1, nums2[p2])
                    p1 += 1
                    m += 1
                    nums2.remove(nums2[p2])
            while len(nums2) > 0:
                nums1.insert(p1, nums2[p2])
                p1 += 1
                nums2.remove(nums2[p2])
            # nums1 = nums1[:m_c + n_c]
            for i in range(len(nums1)-(m_c + n_c)):
                nums1.pop()
        print(nums1)
def test0():
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    s.merge(nums1,m,nums2,n) #[1, 2, 2, 3, 5, 6]

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [0]
    m,n=3,1
    s.merge(nums1,m,nums2,n)#[0, 1, 2, 3]


    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [1]
    m,n=3,1

    s.merge(nums1,m,nums2,n)#[1, 1, 2, 3]


    nums1 = [1, 0]
    nums2 = [1]
    m,n=1,1
    s.merge(nums1,m,nums2,n)#[1, 1]


    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = list()
    m,n=3,0
    s.merge(nums1,m,nums2,n)
    nums1 = []
    nums2 = []
    m,n=0,0
    s.merge(nums1,m,nums2,n)
def test2():
    s = Solution()
    nums1 = [0]
    nums2 = [1]
    m = 0
    n = 1
    s.merge(nums1, m, nums2, n)
    nums1 = [0]
    nums2 = [1,3,4]
    m = 0
    n = 3
    s.merge(nums1, m, nums2, n)
def test3():

    s = Solution()
    nums1 = [1,0]
    nums2 = [2]
    m = 1
    n = 1
    s.merge(nums1, m, nums2, n)
if __name__ == "__main__":

    test0()
    test2()
    test3()