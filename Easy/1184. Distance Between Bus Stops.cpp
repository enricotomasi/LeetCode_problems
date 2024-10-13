class Solution
{
public:
    int distanceBetweenBusStops(vector<int> &distance, int start, int destination)
    {
        int n = distance.size();
        
        int d1 = 0;
        int pos = start;

        while (pos != destination)
        {
            d1 += distance[pos];
            
            // cout << "pos: " << pos << " distance[pos]: " << distance[pos] << " d1: " << d1 << endl;

            pos++;
            pos %= n;
        }

        // cout << "d1: " << d1 << endl << endl;
        
        int d2 = 0;
        pos = start;

        do
        {
            pos--;
            if (pos < 0)
            {
                pos = n - 1;
            }

            d2 += distance[pos];
            
            // cout << "pos: " << pos << " distance[pos]: " << distance[pos] << " d2: " << d2 << endl;
        }
        while (pos != destination);

        // cout << "d2: " << d2 << endl;

        return min(d1, d2);
    }
};