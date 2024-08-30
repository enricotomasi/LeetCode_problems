class Solution
{
public:
    string toGoatLatin(string sentence)
    {
        vector<string> words;
        
        string temp = "";
        for (char c : sentence)
        {
            if (c == ' ' && temp != "")
            {
                words.push_back(temp);
                temp = "";
            }
            else
            {
                temp += c;
            }
        }

        if (temp != "")
        {
            words.push_back(temp);
        }

        string ans = "";
        
        
        int wi = 1;

        for (auto it : words)
        {
            // cout << endl << " *****  " << it << endl;
            string temp = "";
            

            if (ans.length() > 0)
            {
                ans += ' ';
            }

            if (tolower(it[0]) == 'a' || tolower(it[0]) == 'e' || tolower(it[0]) == 'i' || tolower(it[0]) == 'o' || tolower(it[0]) == 'u')
            {
                // cout << "vowel" << endl;
                temp = it + "ma";
            }
            else
            {
                // cout << "consonant" << endl;
                temp = it.substr(1) + it[0] + "ma";
            }

            // cout << "temp: " << temp << endl;
            
            for (int i = 0; i < wi; i++)
            {
                temp += "a";
            }
       
            // cout << "temp after adding 'a': " << temp << endl;

            ans += temp;
            wi++;

        }

        return ans;
    }
};