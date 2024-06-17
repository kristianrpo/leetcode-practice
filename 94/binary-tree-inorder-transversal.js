/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    let list = []
    list = inorderTraversalSolution(root,list)
    if(list){
        return list
    }
    else{
        return []
    }
};

var inorderTraversalSolution = function(root,list) {
    if(root==null){
        return;
    }
    inorderTraversalSolution(root.left,list)
    list.push(root.val)
    inorderTraversalSolution(root.right,list)
    return list
};