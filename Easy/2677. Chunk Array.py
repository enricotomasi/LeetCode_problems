/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size)
{
    ans = [];
    let j = 0;
    temp = [];
    
    for (let i = 0; i < arr.length; i++)
    {
        j++;
        temp.push(arr[i])
        if (j >= size)
        {
            ans.push(temp);
            temp = [];
            j = 0;
        }
    }

    if (temp.length > 0)
    {
        ans.push(temp);
    }
    
    return ans;

};
