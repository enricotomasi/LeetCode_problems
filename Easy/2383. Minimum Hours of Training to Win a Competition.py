class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        en = 0

        while True:
            e = initialEnergy + en

            for it in energy:
                e -= it
            
            if e > 0:
                break
            
            en += 1
        
        xp = 0

        while True:
            x = initialExperience + xp

            ok = True           
            for it in experience:
                if it >= x:
                    ok = False
                    break 
                
                x += it
            
            if ok:
                break
            
            xp += 1


        return en + xp