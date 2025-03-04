class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        first_w = 0
        second_w = 0
        third_w = 0
        fourth_w = 0

        first_b = 0
        second_b = 0
        third_b = 0
        fourth_b = 0

        if grid[0][0] == 'W':
            first_w += 1
        else:
            first_b += 1

        if grid[0][1] == 'W':
            first_w += 1
            second_w += 1
        else:
            first_b += 1
            second_b += 1

        if grid[0][2] == 'W':
            second_w += 1
        else:
            second_b += 1

        if grid[1][0] == 'W':
            first_w += 1
            third_w += 1
        else:
            first_b += 1
            third_b += 1

        if grid[1][1] == 'W':
            first_w += 1
            second_w += 1
            third_w += 1
            fourth_w += 1
        else:
            first_b += 1
            second_b += 1
            third_b += 1
            fourth_b += 1

        if grid[1][2] == 'W':
            second_w += 1
            fourth_w += 1
        else:
            second_b += 1
            fourth_b += 1

        if grid[2][0] == 'W':
            third_w += 1
        else:
            third_b += 1
        
        if grid[2][1] == 'W':
            third_w += 1
            fourth_w += 1
        else:
            third_b += 1
            fourth_b += 1
        
        if grid[2][2] == 'W':
            fourth_w += 1
        else:
            fourth_b += 1

        # print(first_w, second_w, third_w, fourth_w)
        # print(first_b, second_b, third_b, fourth_b)

        if (first_w >= 3 or second_w >= 3 or third_w >= 3 or fourth_w >= 3) or (first_b >= 3 or second_b >= 3 or third_b >= 3 or fourth_b >= 3):
            return True
        
        return False
