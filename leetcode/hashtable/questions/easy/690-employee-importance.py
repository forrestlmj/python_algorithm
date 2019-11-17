"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
import queue
class Solution:
    def findById(self,es,id):
        for e in es:
            if e.id == id:
                return e
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if not employees:
            return 0
        q = queue.deque()
        q.append(id)
        ans = 0
        while q:
            c = q.popleft()
            node = self.findById(employees,c)
            ans += node.importance
            for i in node.subordinates:
                q.append(i)
        return ans