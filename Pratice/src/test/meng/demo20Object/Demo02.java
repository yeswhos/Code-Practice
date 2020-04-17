package test.meng.demo20Object;

import java.util.Objects;

public class Demo02 {
    public static void main(String[] args) {
        String s1 = "abc";
        String s2 = "abc";
        String s3 = null;
        boolean a = s1.equals(s2);
        System.out.println(a);
        //object防止空指针异常
        boolean b = Objects.equals(s1, s3);
        System.out.println(b);
    }
}
