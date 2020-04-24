package test.meng.demo27List;

import java.util.ArrayList;
import java.util.List;

public class Demo00List {
    public static void main(String[] args) {
        //多态创建集合
        List<String> list = new ArrayList<>();
        list.add("a");
        list.add(1, "b");
        list.add("c");

        String s1 = list.remove(0);
        System.out.println(s1);
        list.add(0, "a");

        String s2 = list.set(0, "B");
        System.out.println(s2);

        System.out.println(list);

    }
}
