/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let IndexElement = nums.findIndex((num)=> num===target)
    if (IndexElement !=- 1){
        return IndexElement
    }
    else{
        let elements = []
        for(let i = target-1; i>=nums[0]; i--){
            elements.push(i)
        }
        for(let element of elements){
            let lastIndexElement = nums.lastIndexOf(element)
            let subarrray = nums.slice(0,lastIndexElement)
            if (lastIndexElement!=-1){
                return lastIndexElement+1
            }
        }
        return 0
    }
};
