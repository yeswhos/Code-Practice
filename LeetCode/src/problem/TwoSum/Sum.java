package problem.TwoSum;

public class Sum{
    public static void main(String[] args) {

    }
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length(); i++){
            int a = nums[i];
            for(int j = 0; j < nums.length(); j++){
                if(j != i){
                    int b = nums[j];
                }
                if(a + b == target){
                    return i, j;
                }
            }
        }
    }
}