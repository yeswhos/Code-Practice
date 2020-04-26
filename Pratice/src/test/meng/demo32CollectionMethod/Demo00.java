package test.meng.demo32CollectionMethod;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class Demo00 {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        Collections.addAll(list, 1, 2, 3, 4);
        System.out.println(list);
        Collections.shuffle(list);
        System.out.println(list);
    }
}
