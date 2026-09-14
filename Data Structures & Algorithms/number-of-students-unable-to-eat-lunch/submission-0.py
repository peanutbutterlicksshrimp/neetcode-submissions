class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        go = True

        while students and count < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                val = students.pop(0)
                students.append(val)
                count+=1
            if count == 3:
                print("students", students)
                print("sand", sandwiches)

        print(count)
        return len(students)