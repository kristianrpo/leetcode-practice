/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let number = BigInt(digits.join().replace(/,/g,""))
    number++
    return number.toString().split("")
};