// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution
{
public:
    int firstBadVersion(int n)
    {
        if (n == 1)
        {
            return 1;
        }

        long long int start = 1;
        long long int end = n;

        while (start <= end)
        {
            long long int mid = (start + end) / 2;

            if (isBadVersion(mid))
            {
                if (!isBadVersion(mid - 1))
                {
                    return mid;
                }
                else
                {
                    end = mid - 1;
                }
            }
            else
            {
                start = mid + 1;
            }

        }

        return n;
    }

};