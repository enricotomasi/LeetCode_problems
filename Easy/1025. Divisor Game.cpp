class Solution
{

// hint 1 : If the current number is even, we can always subtract a 1 to make it odd. 
//          If the current number is odd, we must subtract an odd number to make it even.

public:
    bool divisorGame(int n)
    {
        return n % 2 == 0;
    }
};