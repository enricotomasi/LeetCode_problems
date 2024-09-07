class Solution
{
public:
    bool isLongPressedName(string name, string typed)
    {
        if (name[0] != typed[0])
        {
            return false;
        }

        int nn = name.length();
        int nt = typed.length();
        
        // cout << "name: " << name << " " << nn << endl;
        // cout << "type: " << typed << " " << nt << endl;
 
        int in = 1;
        int it = 1;

        if (nn == 1)
        {
            in = 0;
        }

        while (it < nt)
        {
            // cout << endl << "it: " << it << " in: " << in << endl;
            // cout << name[in] << " " << typed[it] << endl;

            if (name[in] == typed[it])
            {
                // cout << "   -> name[in] == typed[it]" << endl;
                if (in < nn - 1) in++;
                it++;
            }
            else
            {
                // cout << "   -> name[in] typed[it]" << endl;
                if (typed[it] == typed[it - 1])
                {
                    // cout << "   -> typed[it] == typed[it - 1]" << endl;
                    it++;
                }
                else
                {
                    // cout << "   -> typed[it] != typed[it - 1] * false * " << endl; 
                    return false;
                }
            }
        }

        // cout << "  **** in: " << in << " nn: " << nn << endl;
        if (in < nn - 1)
        {
            return false;
        }

        return typed[nt - 1] == name[nn - 1];

    }
};