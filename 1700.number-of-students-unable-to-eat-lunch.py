#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start


from typing import Counter


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = Counter(students)
        for sandwich in sandwiches:
            if not students[sandwich]:
                break
            students[sandwich] -= 1
        return sum(students.values())


# @lc code=end
