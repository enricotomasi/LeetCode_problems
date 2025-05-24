class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def gen(o, c, temp):
            if o == 0 and c == 0:
                ans.append("".join(temp))
                return
            
            if o > 0:
                temp.append('(')
                gen(o - 1, c, temp)
                temp.pop()  
            
            if c > o:
                temp.append(')')
                gen(o, c - 1, temp)
                temp.pop()  

        gen(n, n, [])

        return ans
        