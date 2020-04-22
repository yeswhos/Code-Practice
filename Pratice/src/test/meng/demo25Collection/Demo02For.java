package test.meng.demo25Collection;

import java.lang.reflect.Array;
import java.util.ArrayList;

public class Demo02For {
    public static void main(String[] args) {
        int [] a = {1, 2, 3, 4};
        ArrayList<String> b = new ArrayList<String>();
        b.add("1");
        b.add("2");
        b.add("3");
        b.add("4");
        demo00(a);
        demo01(b);

    }
    private static void demo00(int [] a){
        for(int i: a){
            System.out.println("array: " + i);
        }
    }
    private static void demo01(ArrayList<String> a){
        for(String i : a){
            System.out.println("arraylist: " + i);
        }
    }
}
