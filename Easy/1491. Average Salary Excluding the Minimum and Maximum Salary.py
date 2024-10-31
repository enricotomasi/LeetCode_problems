class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        salary.sort()

        temp = 0;
        for i in range(1, n - 1):
            temp += salary[i]
        
        return temp / (n - 2)
        
