class Solution
{
public:
    int isPrefixOfWord(string sentence, string searchWord)
    {
        vector<string> words;
        string temp = "";

        for (char c : sentence)
        {
            if (c == ' ')
            {
                words.push_back(temp);
                temp = "";
            }
            else
            {
                temp += c;
            }
        }
         
        words.push_back(temp);

        int nw = searchWord.length();

        for (int ans = 0; ans < words.size(); ans++)
        {
            // cout << words[ans] << endl;

            if (words[ans].length() < nw)
            {
                // cout << "words[ans].length() < nw" << endl;
                continue;
            }
            
            int i;
            int j = 0;
            
            bool ok = true;
            for (i = 0; i < nw; i++)
            {
                // cout << "  ---> " << searchWord[i] << " == " << words[ans][j] << endl;
                if (searchWord[i] != words[ans][j])
                {
                    // cout << "  ---> " << " false" << endl;
                    ok = false;
                    break;
                }
                j++;
            }

            if (ok)
            {
                return ans + 1;
            }

            
        }

        return -1;

        

    }
};
