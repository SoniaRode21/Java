

/**
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 @author "Soniya Rode"
 */
class 2btEqual {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null && q==null){
            return true;
        }

        if(p!=null && q!=null){
           return p.val==q.val && isSameTree(p.left,q.left) && isSameTree(p.right,q.right); 
        }
        //If either one of them is null(not equal number of nodes)
        return false;
            
        
    }
   

}