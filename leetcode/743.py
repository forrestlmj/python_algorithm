#https://leetcode.com/problems/network-delay-time/
# 使用广度优先搜索
class Solution:


    def adjacencyList(self,N,times):
        a_list = [[] for i in range(0,N+1)]
        for time in times:
            a_list[time[0]].append([time[1], time[2]])
        return a_list[1:]
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        #TODO 最大的问题是目前头一个节点应该为N_bit访问过。
        N_bit = [0 for i in range(0,N)]
        # N_bit[K-1] = 1
        a_list = self.adjacencyList(N,times)
        print(a_list)
        # 栈的数据结构为遍历路径的
        stack = [(K,0)]
        # N_bit[K] = 1
        path_all = []
        max_length = 0
        while(len(stack)>0):
            current_vertex = stack[len(stack)-1][0]
            current_time = stack[len(stack)-1][1]
            stack.pop()
            N_bit[current_vertex-1] = 1

            current_poped_list = sorted(a_list[current_vertex-1],key=lambda i:i[1])
            # 关键：进栈的顺序为累计延时最小的节点先进入栈中
            for i in current_poped_list:
                # 判断是否已经遍历过,在决定加时间
                # if N_bit[current_vertex-1] == 1:
                #     pass
                # if:
                    i[1] = i[1]+current_time
                    if i[1] > max_length:
                        max_length = i[1]
                    stack.append(i)
                    # if N_bit[current_vertex-1] == 0:
                    #     stack.append(i)
                    # else:
                    #     pass

        print(path_all)
        print(N_bit)
        print("最大步数" + str(max_length))

        if sum(N_bit) < N:
            print("不全")
            return -1
        else:
            return max_length
def test():
    times = [[2,1,1],[2,3,1],[3,4,1]]
    N = 4
    K = 2
    s = Solution()
    s.networkDelayTime(times,N,K)
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
    s.networkDelayTime(times,N,K)
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
    s.networkDelayTime(times, N, K)
test2()
