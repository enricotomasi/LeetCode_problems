class Solution
{
public:
    void duplicateZeros(vector<int> &arr)
    {
        int n = arr.size();
        queue<int> q;

        for (int i = 0; i < n; i++)
        {
            q.push(arr[i]);
        }

        for (int i = 0; i < n; i++)
        {
            cout << "q.front(): " << q.front() << endl;
            if (q.front() == 0)
            {
                arr[i] = 0;
                if (i < n - 1) arr[i + 1] = 0;
                i++;
            }
            else
            {
                arr[i] = q.front();
            }

            q.pop();
        }
        
    }
};
