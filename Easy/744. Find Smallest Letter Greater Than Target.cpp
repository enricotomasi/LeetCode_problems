class Solution
{
public:
    char nextGreatestLetter(vector<char> &letters, char target)
    {
        int n = letters.size();
        char ans = letters[0];

        if (ans == target)
        {
            int i = 1;
            while (i < n && letters[i] == target)
            {
                i++;
            }
            return letters[i];
        }

        int start = 0;
        int end = n - 1;

        while (start <= end)
        {
            int mid = (start + end) / 2;
            // cout << "start : " << start << " end: " << " mid: " << mid << " letters[mid]: " << letters[mid] << " ans: " << ans << endl;
            if (letters[mid] <= target)
            {
                start = mid + 1;
            }
            else
            {
                ans = letters[mid];
                end = mid - 1;
            }

        }

        return ans;
    }
};