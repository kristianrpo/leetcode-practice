/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let i=0;
    let j=1;
    let positions = [];
    while(i<nums.length){
        while(j<nums.length){
            if (((nums[i]+nums[j]) === target) && (i!=j)){
                positions.push(i)
                positions.push(j)
                return positions
            }
            j++
        }
        i++
        j=0
    }
    return positions
};