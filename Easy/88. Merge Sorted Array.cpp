
class Solution 
{
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n)
    {     
        vector<int> final;

        int i = 0;
        int j = 0;

        while (i < m || j < n)
        {
            // cout << endl << "i: " << i << " m:" << m << " j: " << j << " n:" << n << endl;
            if (i >= m)
            {
                // cout << "i >= m || nums1[i] == 0" << endl;
                final.push_back(nums2[j]);
                j++;
            }
            else if (j >= n)
            {
                // cout << "j >= n" << endl;
                final.push_back(nums1[i]);
                i++;
            }
            else
            {
                // cout << "else" << endl;
                if (nums1[i] >= nums2[j])
                {
                    // cout << "nums1[i] >= nums2[j]" << endl;
                    final.push_back(nums2[j]);
                    j++;
                }
                else
                {
                    cout << "else" << endl;
                    final.push_back(nums1[i]);
                    i++;
                }
            }          
            
            // for (auto it : final) cout << it << " ";
            // cout << endl;
        }

        for (int i = 0; i < final.size(); i++)
        {
            nums1[i] = final[i];
        }

    }
};