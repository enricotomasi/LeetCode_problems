class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while len(students) > 0:
            if students[0] == sandwiches[0]:
                students = students[ 1 : ]
                sandwiches = sandwiches[ 1 : ]
            else:
                students += [students[0]]
                students = students[ 1 : ]

                if sandwiches[0] not in students:
                    return len(students)
        
        return len(students)