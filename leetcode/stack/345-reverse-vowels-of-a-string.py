import queue
class Solution:
    def reverseVowels(self, s: str) -> str:
        st = queue.deque()
        alh = "aeiouAEIOU"
        s = list(s)
        for i in range(len(s)):
            if s[i] in alh:
                st.append(s[i])
                s[i] = None
        print(st)
        for i in range(len(s)):
            if not s[i]:
                s[i] = st.pop()
        return "".join(s)