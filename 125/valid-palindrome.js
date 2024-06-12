/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let sWithoutSpaces = s.toLocaleLowerCase().replace(/[\x20-\x2F\x3A-\x40\x5B-\x60\x7B\x7D]/g, '')
    let sReversed = sWithoutSpaces.split("").reverse().join("")
    console.log(sWithoutSpaces)
    if (sReversed==sWithoutSpaces){
        return true
    }
    else{
        return false
    }
};