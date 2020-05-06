/*
 14. Longest Common Prefix
 Write a function to find the longest common prefix string amongst an array of strings.
    
 If there is no common prefix, return an empty string "".
    
 Example 1:

 Input: ["flower","flow","flight"]
 Output: "fl"
 Example 2:

 Input: ["dog","racecar","car"]
 Output: ""
 Explanation: There is no common prefix among the input strings.
     Note:

 All given inputs are in lowercase letters a-z.
 */

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    let result = "";
    if (!strs.length) return result;
    let first = strs[0];
    for (let i = 0; i < first.length; ++i) {
        for (let j = 1; j < strs.length; ++j) {
            if (strs[j][i] !== first[i]) return result;
        }
        result += first[i];
    }
    return result;
};

const testCases = [
    ["dog", "racecar", "car"],
    ["flower", "flow", "flight"],
    [],
]

testCases.forEach((test) => {
    console.log(test, longestCommonPrefix(test));
})
