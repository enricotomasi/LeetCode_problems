/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var rowAndMaximumOnes = function(mat)
{
    const m = mat.length;
    const n = mat[0].length;
    
    let row = -1;
    let nones = -1;

    for (let i = 0; i < m; i++)
    {
        let tempone = 0;
        for (let j = 0; j < n; j++)
        {
            if (mat[i][j] == 1)
            {
                tempone += 1;
            }
        }

        if (tempone > nones)
        {
            nones = tempone;
            row = i;
        }

    }

    return [row, nones];

};