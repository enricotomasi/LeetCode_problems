class Solution
{
public:
    int maxNumberOfBalloons(string text)
    {
        int c[26] = { };

        for (char it : text)
        {
            c[it - 'a']++;
        }

        // for (int i = 0; i < 26; i++) cout << "i : " << i << " " << (char)(i + 'a') << endl;
        // i : 0 a
        // i : 1 b
        // i : 11 l
        // i : 13 n
        // i : 14 o

        return min(c[0], min(c[1], min(c[11] / 2, min(c[13], c[14] / 2))));

    }
};