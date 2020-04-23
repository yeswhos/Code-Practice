package problem.MergeTwoBinaryTree;
import java.lang.System;

import javax.swing.tree.TreeNode;

public class BinaryTreeDemo {

    public void test() {
        TreeNode leftTree = new TreeNode(1);
        leftTree.left = new TreeNode(3);
        //leftTree.right = new TreeNode(4);

        
        TreeNode rightTree = new TreeNode(2);
        //rightTree.left = new TreeNode(5);
        rightTree.right = new TreeNode(6);


        TreeNode result = mergeTrees(leftTree, rightTree);
        result.print();
    }

    private TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        return calculate(t1,t2);
        
    }

    private TreeNode calculate(TreeNode t1, TreeNode t2){
        if(t1 != null && t2 != null){
            TreeNode result = new TreeNode(t1.val + t2.val);
            result.left = calculate(t1.left, t2.left);
            result.right = calculate(t1.right, t2.right);
            return result;
        }
        else if(t1 != null && t2 == null){
            TreeNode result = new TreeNode(t1.val);
            result.left = calculate(t1.left, null);
            result.right = calculate(t1.right, null);
            return result;
        }
        else if(t1 == null && t2 != null){
            TreeNode result = new TreeNode(t2.val);
            result.left = calculate(null, t2.left);
            result.right = calculate(null, t2.right);
            return result;
        }
        else{
            return null;
            
        }
    }

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        public TreeNode(int x) {
             val = x; 
        }
        public void print() {
            System.out.println(" - " + val);
            if (left != null)
                left.print();
            if (right != null)
                right.print();
        }
    }
}