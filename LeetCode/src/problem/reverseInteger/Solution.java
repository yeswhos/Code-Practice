package problem.reverseInteger;

import java.util.ArrayList;

public class Solution {
    public static void main(String[] args) {
        int x = 1563847412;
        int result = reverse(x);
        System.out.println(result);
    }
    public static int reverse(int x){
        int len = 0;
        if(x < 0){
            len = (x + "").length() - 1;
        }
        else if(x > 2147483647){
            return 0;
        }
        else {
            len = (x + "").length();
        }
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i < len; i++){
            int j = x % 10;
            x = x / 10;
            list.add(j);

        }
        System.out.println(list);
        double test = 0;
        int result = 0;
        for(int i = 0; i < list.size(); i++){

            long a = (long)Math.pow(10, len - i - 1);

            //System.out.println(a);
            test += list.get(i) * a;
            //System.out.println(result);
        }
        if((test < -2147483647) ||(test > 2147483647)){
            return 0;
        }
        else{
            result = (int) test;
        }
        //System.out.println(list);
        return result;
    }
}
