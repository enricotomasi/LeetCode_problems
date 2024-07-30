/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution
{
public:
    int guessNumber(int n)
    {        
        long long int start = 0;
        long long int end = n;

        while (start <= end)
        {
            // cout << endl;
            // cout << "--------------------------------------------------------------------------" << endl;
            
            // cout << "start + end / 2 = " << ((start + end) / 2) << endl;
            
            long long int mid = (start + end) / 2;

            // cout << endl << "start: " << start << " end: " << end << " mid: " << mid << endl;

            int g = guess(mid);

            if (g == 0)
            {
                return mid;
            }
            else if (g == -1)
            {
                end = mid - 1;
            }
            else
            {
                start = mid + 1;
            }

            // cout << "start: " << start << " end: " << end << endl;
            // cout << "--------------------------------------------------------------------------" << endl;
        }

        return n;

    }
};