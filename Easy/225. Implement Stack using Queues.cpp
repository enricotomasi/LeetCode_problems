class MyStack
{
public:
    queue<int> q;
    MyStack()
    {
        q = queue<int>();
    }
    
    void push(int x)
    {
        if (q.empty())
        {
            q.push(x);
            return;
        }

        queue<int> temp;

        while (!q.empty())
        {
            temp.push(q.front());
            q.pop();
        }

        q = queue<int>();

        q.push(x);

        while (!temp.empty())
        {
            q.push(temp.front());
            temp.pop();
        }

    }
    
    int pop()
    {
        if (q.empty())
        {
            return NULL;
        }
        
        queue<int> temp;

        while (!q.empty())
        {
            temp.push(q.front());
            q.pop();
        }

        q = queue<int>();

        int ans = temp.front();
        temp.pop();

        while (!temp.empty())
        {
            q.push(temp.front());
            temp.pop();
        }

        return ans;
    }
    
    int top()
    {
        if (q.empty())
        {
            return NULL;
        }
        
        queue<int> temp;

        while (!q.empty())
        {
            temp.push(q.front());
            q.pop();
        }

        q = queue<int>();

        int ans = temp.front();

        while (!temp.empty())
        {
            q.push(temp.front());
            temp.pop();
        }

        return ans;
    }
    
    bool empty()
    {
        return q.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */