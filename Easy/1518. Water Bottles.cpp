class Solution 
{
public:
    int numWaterBottles(int numBottles, int numExchange) 
    {
        int full = numBottles;
        int empty = 0;

        int ans = 0;

        while (full + empty> 0 && (full + empty) / numExchange > 0)
        {
            //cout << endl << "1# full: " << full << " empty: " << empty << " ans: " << ans << endl;

            // drink
            ans += full;
            empty += full;
            full = 0;

            //cout << "2# full: " << full << " empty: " << empty << " ans: " << ans << endl;

            // Exchange
            full = empty / numExchange;
            empty = empty % numExchange;

            //cout << "3# full: " << full << " empty: " << empty << " ans: " << ans << endl;

        }
        
        //cout << endl << "Exit, full: " << full << " ans: " << ans << endl;

        return ans + full;      
        
    }
};