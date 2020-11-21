/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  const parentheses = {'}': '{', ']': '[', ')': '('};
  let leftParentheses = [];
  let i = 0;
  let result = true;

  while (i < s.length && result) {
    if (!parentheses[s[i]]) {
      leftParentheses.push(s[i]);
    } else if (leftParentheses.pop() !== parentheses[s[i]]) {
      result = false;
    }
    i++;
  }

  return result && !leftParentheses.length;
};

console.log(isValid('()'), true);
console.log(isValid('()[]{}'), true);
console.log(isValid('()[]{}'), true);
console.log(isValid('(]'), false);
console.log(isValid('([)]'), false);
console.log(isValid('{[]}'), true);
console.log(isValid('{'), false);
console.log(isValid('}'), false);
