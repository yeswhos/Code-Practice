package test.meng.demo20Object;

import java.util.ArrayList;

public class Demo01 {
    public static void main(String[] args) {
        Demo00 demo00 = new Demo00("Yasuo", 33);
        //Demo00 demo01 = new Demo00("Draven", 23);
        Demo00 demo01 = new Demo00("Yasuo", 33);
        System.out.println(demo00);
        System.out.println(demo01);
        ArrayList list = new ArrayList();
        System.out.println(demo00.equals(list));
        System.out.println(demo00.equals(null));
        System.out.println(demo00.equals(demo00));
        System.out.println(demo00.equals(demo01));

    }
}
