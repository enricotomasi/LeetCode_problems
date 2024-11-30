class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0

        for it in items:
            if (ruleKey == "type" and it[0] == ruleValue) or (ruleKey == "color" and it[1] == ruleValue) or (ruleKey == "name" and it[2] == ruleValue):
                ans += 1
                
        return ans
        