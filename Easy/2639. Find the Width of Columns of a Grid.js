/**
 * @param {number[][]} grid
 * @return {number[]}
 */

let len = function(n)
{
    if (n == 0)
    {
        return 1;
    }

    ans = 0;

    if (n < 0)
    {
        ans = 1;
        n = n * -1;
    }

    ans += Math.trunc(Math.log10(n)) + 1;

    return ans;

};

var findColumnWidth = function(grid)
{
    let m = grid.length;
    let n = grid[0].length;

    console.log(len(0));

    let ans = [];
    
    for (let i = 0; i < n; i++)
    {
        let lencol = -1;

        for (let j = 0; j < m; j++)
        {
            lencol = Math.max(lencol, len(grid[j][i]));
        }
        
        ans.push(lencol);
    }

    return ans;
};