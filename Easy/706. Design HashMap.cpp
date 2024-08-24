class MyHashMap
{
public:
    vector<vector<int>> v;
    // void debugprint()
    // {
    //     cout << "---------------------------" << endl;
        
    //     for (int i = 0; i < v.size(); i++)
    //     {
    //         cout << i << "#  " << v[i][0] << ", " << v[i][1] << endl;
    //     }
        
    //     cout << "---------------------------" << endl;
    // }
    
    MyHashMap()
    {
        v = vector<vector<int>>();
    }
    
    void put(int key, int value)
    {
        // cout << endl << "put: " << key << ", " << value << endl;
        // debugprint();

        int pos = find(key);
        if (pos < 0)
        {
            vector<int> temp;
            temp.push_back(key);
            temp.push_back(value);
            v.push_back(temp);
        }
        else
        {
            v[pos] = {key, value};
        }
    }
    
    int get(int key)
    {
        // cout << endl << "get: " << key << endl;
        
        for (int i = 0; i < v.size(); i++)
        {
            if (v[i][0] == key)
            {
                // cout << v[i][1] << endl;
                return v[i][1];
            }
        }
        
        // cout << "-1" << endl;
        
        return -1;
    }
    
    void remove(int key)
    {
        // cout << endl << "remove: " << key << endl;
        // debugprint();
        
        int pos = find(key);
        if (pos < 0)
        {
            return;
        }

        v.erase(v.begin() + pos);
    }

    int find(int key)
    {
        for (int i = 0; i < v.size(); i++)
        {
            if (v[i][0] == key)
            {
                return i;
            }
        }

        return -1;
    }

};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */