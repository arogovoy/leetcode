/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  let indexA = 0;
  let indexB = nums.length - 1;
  while(nums[indexA] + nums[indexB] !== target) {
    indexB--;
    if (indexB === indexA) {
      indexA++;
      indexB = nums.length
    }
  }

  return [indexA, indexB];
};

console.log(twoSum([2, 7, 11, 15], 9));
