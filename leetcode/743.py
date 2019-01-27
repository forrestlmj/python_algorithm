#https://leetcode.com/problems/network-delay-time/

class Solution:


    def adjacencyList(self,N,times):
        a_list = [[] for i in range(0,N+1)]
        for time in times:
            a_list[time[0]].append({"N_node":time[1],"length":time[2]})
        return a_list[1:]
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        max_time = -1
        N_bit = [0 for i in range(0,N)]
        a_list = self.adjacencyList(N,times)
        print(a_list)
        stack = [K]
        path=list()
        path.append(K)
        length = 0
        all_path = list()
        while(len(stack)>0):
            current_node = stack[len(stack)-1]
            stack.pop()



            for i in a_list[current_node-1]:
                stack.append(i["N_node"])
                # path_all.append(current_vertex)
                # 计算路径时可能会有问题
                for path in all_path:
                    path.append(i["N_node"])
                    length+=i["length"]



            print(current_node)
            N_bit[current_node-1] = 1
        # print(path_all)
        print(N_bit)
        if sum(N_bit) < N:
            print("-1")
            return -1
        else:
            return "path"
def test():
    times = [[2,1,1],[2,3,1],[3,4,1]]
    N = 4
    K = 2
    s = Solution()
    s.networkDelayTime(times,N,K)
def test2():
    N = 7
    K = 1
    times = [[1,5,7],
             [3,2,6],
             [1,6,2],
             [1,4,5],
             [2,7,33],
             [3,1,2],
             [7,6,2],
             [5,4,5],
             [4,7,1]]
    s = Solution()
    s.networkDelayTime(times,N,K)
test()
test2()
