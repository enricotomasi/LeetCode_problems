class Solution
{
public:
    bool canPlaceFlowers(vector<int> &flowerbed, int n)
    {
        int last = 0;
        int nf = flowerbed.size();

        for (int i = 0; i < nf; i++)
        {
            // cout << endl << i << "# flowerbed[i]: " << flowerbed[i] << " last: " << last<< endl;
            if (n < 0)
            {
                // cout << "n < 0, all planted!" << endl;
                return true;
            }

            int next = 0;
            if (i < nf - 1)
            {
                next = flowerbed[i + 1];
                // cout << " * set next" << endl;
            }

            // cout << "next: " << next << endl;

            if (last == 1 || next == 1)
            {
                // cout << "last == 1 || next = 1, continue" << endl;
                last = flowerbed[i];
            }
            else
            {
                // cout << "last == 0" << endl;
                if (flowerbed[i] == 0)
                {
                    // cout << " ### PLANT! ### flowebed == 0" << endl;
                    n--;
                    last = 1;
                }
                else
                {
                    last = flowerbed[i];
                }
            }

            // cout << "n: " << n << endl;
        }

        // cout << endl << " **** n: " << n << endl;
        
        return n <= 0;

    }
};