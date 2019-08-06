/*
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

*/

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
  var result = '';
  var t = Math.abs(x);
  var sign = Math.sign(x) >= 0 ? 1 : -1;

  function checkRange(value) {
    return value <= -2147483648 || value >= 2147483647 ? 0 : value;
  }

  if (!(checkRange(x))) {
    return 0;
  }

  while (t) {
    result += t % 10;
    t = Math.floor(t / 10);
  }

  return checkRange(Number(result) * sign);
};

console.log(reverse(123));
console.log(reverse(120));
