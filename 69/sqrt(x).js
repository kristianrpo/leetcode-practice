/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    xSqrt = Math.sqrt(x)
    decimals = xSqrt%1
    xSqrt = xSqrt-decimals
    return Math.floor(xSqrt)
};