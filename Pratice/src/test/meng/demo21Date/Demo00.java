package test.meng.demo21Date;

import java.util.Date;

public class Demo00 {
    public static void main(String[] args) {
        Date date = new Date();
        long a = date.getTime();
        Date date1 = new Date(a);
        System.out.println(date);
        System.out.println(date1);
    }
}
