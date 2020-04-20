package test.meng.demo24Class;

import java.util.ArrayList;

public class Demo01 {
    public static void main(String[] args) {
        Integer a = 1;
//    Integer a = new Integer(1);

        a = a.intValue() + 1;
        System.out.println(a);

        ArrayList<Integer> list = new ArrayList<>();
        list.add(1);
        System.out.println(list.get(0));
    }

}
