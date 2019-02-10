#https://leetcode.com/problems/keys-and-rooms/
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        Opened = [False for i in range(len(rooms))]
        stack_key_useful = list()
        Opened[0] = True

        if len(rooms[0]) == 0 and len(rooms) == 0:
            return False
        else:
            for key in rooms[0]:
                stack_key_useful.append(key)
        while len(stack_key_useful) > 0:
            current_key = stack_key_useful.pop()
            if not Opened[current_key]:
                # 打开门
                Opened[current_key] = True
                # 查找新钥匙
                for key_in_room in rooms[current_key]:
                    # 获取没开门的钥匙
                    if not Opened[key_in_room]:
                        stack_key_useful.append(key_in_room)
                    else:
                        pass
            else:
                # 开过了,钥匙没有用处
                pass
        for o in Opened:
            if not o:
                return False
        return True
def test_0():
    t1 = [[1],[2],[3],[]]
    t2 = [[1,3],[3,0,1],[2],[0]]
    s = Solution()
    assert s.canVisitAllRooms(t1) == True
    assert s.canVisitAllRooms(t2) == False

def test_206438222():
# https://leetcode.com/submissions/detail/206438222/
    t1 = [[],[1]]
    t2 = [[]]
    s = Solution()
    assert s.canVisitAllRooms(t1) == False
    assert s.canVisitAllRooms(t2) == True
if __name__ == "__main__":
    test_0()
    test_206438222()