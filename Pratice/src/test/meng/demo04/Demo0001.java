package test.meng.demo04;

import java.util.Scanner;

public class Demo0001 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        int num1 = 0;
        int num2 = 0;
        char[] b = a.toCharArray();

        for(int i = 0; i < b.length; i++){
            char c = b[i];
            if('A' <= c && c <= 'Z'){
                num1 += 1;
            }
            else if('0' <= c && c <= '9'){
                num2 += 1;
            }
        }
        System.out.println(num1 + "哈" + num2);


    }

}
