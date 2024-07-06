class Solution 
{
public:
    int passThePillow(int n, int time)
    {   
        if ((time / (n - 1)) % 2 != 0)
        {
            //cout << "even" << endl;
            return n - (time % (n - 1));
        }
        
        //cout << "odd" << endl;
        return (time % (n - 1)) + 1;

    }
};