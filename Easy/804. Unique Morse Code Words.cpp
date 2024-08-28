class Solution
{
public:
    int uniqueMorseRepresentations(vector<string> &words)
    {
        string morse[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
                          "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--",
                          "-..-","-.--","--.."};

        set<string> s;

        for (auto it : words)
        {
            string conv = "";

            for (char c : it)
            {
                conv += morse[c - 'a'];
            }

            s.insert(conv);
        }

        return s.size();
    }
};