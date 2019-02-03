#https://leetcode.com/problems/network-delay-time/

class Solution:


    def adjacencyList(self,N,times):
        a_list = [[] for i in range(0,N+1)]
        for time in times:
            a_list[time[0]].append({"N_node":time[1],"length":time[2]})
        return a_list
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        max_time = -1
        N_bit = [float('inf') for i in range(0,N+1)]
        N_bit[K] = 0
        a_list = self.adjacencyList(N,times)
        print(a_list)
        stack = [K]

        while(len(stack)>0):
            current_node = stack[len(stack)-1]
            stack.pop()
            for i in a_list[current_node]:
                # 如果点还没有访问过,那么加入栈中,否则不妨问
                if N_bit[i["N_node"]] == float('inf') or N_bit[i["N_node"]] > N_bit[current_node] + i["length"]:
                    stack.append(i["N_node"])
                    print(i)

                    if N_bit[i["N_node"]] > N_bit[current_node] + i["length"]:
                        N_bit[i["N_node"]] = N_bit[current_node] + i["length"]
            print(current_node)

            # N_bit[current_node-1] = 1
        # print(path_all)
        print(N_bit)
        amax = max(N_bit[1:])
        if amax == float('inf'):
            print("-1")
            return -1
        else:
            print(amax)
            return amax
def test():
    times = [[2,1,1],[2,3,1],[3,4,1]]
    N = 4
    K = 2
    s = Solution()

    assert s.networkDelayTime(times,N,K) == 2

# test2为不包含环图的情况
def test2():
    N = 7
    K = 1
    times = [[1,5,1],
             [3,2,6],
             [1,6,2],
             [1,4,5],
             [2,7,33],
             [3,1,2],
             # [7,6,2],
             # [5,4,5],
             # [7,4,4],
             [4,2,11]
             ]
    s = Solution()
    # 步数应该为49
    assert s.networkDelayTime(times,N,K) == -1
# test3为包含环路图的情况
def test3():
    N = 3
    K = 1
    times = [[1, 2, 1],
             [2, 3, 6],
             [3, 1, 7],

             ]
    s = Solution()
    s.networkDelayTime(times, N, K)
# test()
def test4():
    N = 2
    K = 1
    times = [[1, 2, 1],
             [2, 1, 6],

             ]
    s = Solution()
    s.networkDelayTime(times, N, K)
def test5():
    N = 2
    K = 2
    times = [[1, 2, 1], [2, 1, 3]]
    s = Solution()
    assert s.networkDelayTime(times, N, K) == 3
def test_204431823():
    # https://leetcode.com/submissions/detail/204431823/
    N = 3
    K = 1
    times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
    s = Solution()
    assert s.networkDelayTime(times, N, K) == 3
test()
test2()
test3()
test4()
test5()
test_204431823()