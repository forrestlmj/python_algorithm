#https://leetcode.com/problems/network-delay-time/

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
        N_bit = [0 for i in range(0,N)]
        a_list = self.adjacencyList(N,times)
        print(a_list)
        # 栈的数据结构为遍历路径的
        stack = [(K,0)]
        path_all = []
        max_length = 0
        while(len(stack)>0):
            current_vertex = stack[len(stack)-1][0]
            current_time = stack[len(stack)-1][1]
            stack.pop()
            current_poped_list = sorted(a_list[current_vertex-1],key=lambda i:i[1])
            if len(current_poped_list) == 0:
                pass
            # 关键：进栈的顺序为累计延时最小的节点先进入栈中
            for i in current_poped_list:
                # current_time = current_time+i[1]
                i[1] = i[1]+current_time
                if i[1] > max_length:
                    max_length = i[1]
                    # current_node = i[0]
                stack.append(i)

            N_bit[current_vertex-1] = 1
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
# test2在无环图可以通过
def test2():
    N = 7
    K = 7
    times = [[1,5,1],
             [3,2,6],
             [1,6,2],
             [1,4,5],
             [2,7,33],
             [3,1,2],
             [7,6,2],
             [5,4,5],
             [7,4,4],
             # [4,2,11]
             ]
    s = Solution()
    s.networkDelayTime(times,N,K)
def test3():
    N = 3
    K = 1
    times = [[1, 2, 1],
             [1, 3, 6],
             [2, 3, 7],

             ]
    s = Solution()
    s.networkDelayTime(times, N, K)
# test()
test3()
