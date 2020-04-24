package problem.reverseInteger;

import java.util.ArrayList;

public class Solution {
    public static void main(String[] args) {
        int x = -123;
        int result = reverse(x);
        System.out.println(result);
    }
    public static int reverse(int x){
        int len = (x + "").length();
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i < len; i++){

            int j = x % 10;
            x = x / 10;
            list.add(j);
        }
        int result = 0;
        for(int i = 0; i < list.size(); i++){
            double a = Math.pow(10, len - i - 1);
            System.out.println(a);
            result += list.get(i) * a;
            //System.out.println(result);
        }
        //System.out.println(list);
        return result;
    }
}
