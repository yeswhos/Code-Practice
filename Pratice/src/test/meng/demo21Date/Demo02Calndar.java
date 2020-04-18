package test.meng.demo21Date;

import java.util.Calendar;
import java.util.Date;

public class Demo02Calndar {
    public static void demo00(){
        Calendar calendar = Calendar.getInstance();
        int a = calendar.get(Calendar.YEAR);
        System.out.println("get(): " + a);
    }
    public static void demo01(){
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.YEAR, 2019);
        int a = calendar.get(Calendar.YEAR);
        System.out.println("set(): " + a);
    }

    public static void demo02(){
        Calendar calendar = Calendar.getInstance();
        calendar.add(Calendar.YEAR, 10);
        int a = calendar.get(Calendar.YEAR);
        System.out.println("add(): " + a);
    }

    public static void demo03(){
        Calendar calendar = Calendar.getInstance();
        Date date = calendar.getTime();
        System.out.println("date(): " + date);
    }

    public static void main(String[] args) {
        demo00();
        demo01();
        demo02();
        demo03();

    }

}
