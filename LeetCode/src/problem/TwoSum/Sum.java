package problem.TwoSum;

import java.util.ArrayList;

public class Sum{
    public static void main(String[] args) {
        int [] arr = {2, 7, 11, 15};
        int target = 9;
        int [] result = twoSum(arr, target);
        for(int i = 0; i < result.length; i++){
            System.out.println(i);
        }

    }
    public static int[] twoSum(int[] nums, int target) {
        int result [] = new int [2];
        for(int i = 0; i < nums.length; i++){
            int a = nums[i];
            for(int j = 0; j < nums.length && j != i; j++){
                int b = nums[j];

                if(a + b == target){
//                    System.out.println(i);
//                    System.out.println(j);
                    result[0] = i;
                    result[1] = j;
                    break;
                }
            }
        }

        return result;
    }
}