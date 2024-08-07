class Solution
{
public:
        
    vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
    {
        int n1 = nums1.size();
        int n2 = nums2.size();

        unordered_map<int, int> m;

        for (int i = 0; i < n2; i++)
        {
            m[nums2[i]] = i;
        }

        vector<int> ans;

        for (int i = 0; i < n1; i++)
        {
            // cout << endl << i << " # nums1[i]: " << nums1[i] << endl;

            int index = m[nums1[i]];

            // cout << "index in nums2: " << index << endl;

            int temp = -1;
            
            for (int j = index + 1; j < n2; j++)
            {
                if (nums2[j] > nums1[i])
                {
                    temp = nums2[j];
                    break;
                }
            }            
            
            ans.push_back(temp);
           
        }

        return ans;
    }
};