/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 *
 * @typedef {Object} ListNode
 * @property {number} val
 * @property {ListNode | null} next
 */

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function (l1, l2) {

  if (!l1 && !l2) {
    return null;
  }

  let v1 = l1 ? l1.val : 0;
  let v2 = l2 ? l2.val : 0;

  if (l1 && (v1 <= v2 || !l2)) {
    return {
      val: v1,
      next: mergeTwoLists(l1.next, l2)
    };
  }

  return {
    val: v2,
    next: mergeTwoLists(l1, l2 && l2.next)
  };
};

// const a = {val: 1, next: {val: 2, next: {val: 4}}};
// const b = {val: 1, next: {val: 3, next: {val: 4}}};

// const a = {val: -9, next: {val: 3}};
// const b = {val: 5, next: {val: 7}};

const a = {val: 1};
const b = null;

const res = mergeTwoLists(a, b);

function r (l) {
  let res = [];
  let cur = l;
  while (cur) {
    res.push(cur.val);
    cur = cur.next;
  }
  return res;
}

console.log(r(res));
