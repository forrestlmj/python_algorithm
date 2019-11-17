class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        此题也可以使用字典顺序分组进行，
        :param name:
        :param typed:
        :return:
        """
        n,t = 0, 0
        while n < len(name) and t<len(typed):
            if name[n] == typed[t]:
                pass
            else:
                return False
            while t<len(typed)-1 and n<len(name)-1:
                if typed[t+1] == typed[t] and name[n+1] != name[n]:
                    t += 1
                else:
                    break
            n+=1
            t+=1
        return n == len(name)