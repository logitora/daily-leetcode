"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
"""
class Solution:
    def build(self, n, prereqs):
        adj_list = [[] for _ in range(n)]
        for c1, c2 in prereqs:
            adj_list[c2].append(c1)
        return adj_list
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = self.build(numCourses, prerequisites)
        visited = set()

        def has_cycle(course, stack):
            if course in visited:
                if course in stack:
                    return True
                return False

            visited.add(course)
            stack.append(course)

            for prereq in adj[course]:
                if has_cycle(prereq, stack):
                    return True
            stack.pop()
            return False

        for course in range(numCourses):
            if has_cycle(course, []):
                return False
        return True
"""
This method establishes a helper function to create an adjacency list, which is a matrix showing the relationship between different courses. In this case, 
it shows which course is a needed to take the other. For example, adj[2][1] means that course 1 must be taken before taking course 2. DFS/a method similar to DFS is performed by
following the trail of courses that we end up on. This solution is basically checking if the graph has a cycle or not. We check if the graph is cyclic/acyclic by
utilizing a visited set and a stack. If a course is added to the stack and has not been popped out before it is encountered again, then there is a loop, 
making the course schedule impossible. 
Time = O(n) 
Visited = O(n) Worst case scenario is every option in visited and everything in stack, making this solution a steep linear graph
"""