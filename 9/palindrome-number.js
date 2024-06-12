/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let xString = x.toString()
    let xStringReverse = xString.split('').reverse().join('')
    if (xString===xStringReverse){
        return true
    }
    else{
        return false
    }
};