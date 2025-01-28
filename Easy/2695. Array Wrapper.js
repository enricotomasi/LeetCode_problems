/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums)
{
    this.n = nums;    
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function()
{
    let ans = 0;

    for (let i = 0; i < this.n.length; i++)
    {
        ans += this.n[i];
    }
    return ans;   
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function()
{
    return "[" + this.n.join(",") + "]";    
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
