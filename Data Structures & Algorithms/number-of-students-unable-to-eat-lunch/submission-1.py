
class Solution:


    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        total = len(students)
        count = Counter(students)

        for s in sandwiches:
            if count[s] > 0:
                count[s] -=1
                total -=1
            else:
                return total
        return total

        #BF
        # count = 0
        # go = True

        # while students and count < len(students):
        #     if students[0] == sandwiches[0]:
        #         students.pop(0)
        #         sandwiches.pop(0)
        #         count = 0
        #     else:
        #         val = students.pop(0)
        #         students.append(val)
        #         count+=1
        # return len(students)