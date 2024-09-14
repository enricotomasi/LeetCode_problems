
class Solution
{
public:
    int largestPerimeter(vector<int> &nums)
    {
        int n = nums.size();
        sort(nums.begin(), nums.end());

        for (int i = n - 1; i > 1; i--)
        {
            int a = nums[i];
            int b = nums[i - 1];
            int c = nums[i - 2];

            // cout << i  << "# " << a << " " << b << " " << c << endl;

            if (a < b + c && b < a + c && c < a + b)
            {
                return a + b + c;
            }
        }

        return 0;

    }
};