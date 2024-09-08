class Solution
{
public:
    bool validMountainArray(vector<int> &arr)
    {
        int n = arr.size();

        if (n < 3)
        {
            return false;
        }

        int inc = true;

        for (int i = 0; i < n - 1; i++)
        {
            // cout << endl << i << "#     inc: " << inc << endl;
            if (inc)
            {
                // cout << "   inc" << endl;
                if (arr[i] == arr[i + 1])
                {
                    // cout << "   arr[i] == arr[i + 1] -> false" << endl;
                    return false;
                }
                else if (arr[i] > arr[i + 1])
                {
                    // cout << "   arr[i] > arr[i + 1] -> inc = false" << endl;
                    if (i < 1)
                    {
                        return false;
                    }
                    inc = false;
                }
            }
            else // dec
            {
                // cout << "       dec" << endl;
                if (arr[i] <= arr[i + 1])
                {
                    // cout << "       arr[i] <= arr[i + 1] - > false" << endl;
                    return false;
                }
            }
        }

        // cout << endl << "end, inc: " << inc << endl;

        return !inc;

    }
};