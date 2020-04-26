package test.meng.demo32CollectionMethod;

import java.util.ArrayList;
import java.util.Collections;

public class Demo01 {
    public static void main(String[] args) {
        ArrayList<Integer> list01 = new ArrayList<>();
        Collections.addAll(list01, 2,3,1,5,0);
        Collections.sort(list01);
        System.out.println(list01);

        Demo02Person p1 = new Demo02Person(23, "Fanhui");
        Demo02Person p2 = new Demo02Person(21, "Lulu");
        ArrayList<Demo02Person> list02 = new ArrayList<>();
        Collections.addAll(list02, p1, p2);
        System.out.println(list02);
        Collections.sort(list02);
        System.out.println(list02);
    }
}
