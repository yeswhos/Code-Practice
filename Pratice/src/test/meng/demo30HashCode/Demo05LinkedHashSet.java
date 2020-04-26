package test.meng.demo30HashCode;

import java.util.LinkedHashSet;


public class Demo05LinkedHashSet {
    public static void main(String[] args) {
        LinkedHashSet<String> linked = new LinkedHashSet<>();
        linked.add("www");
        linked.add("meng");
        linked.add("com");
        linked.add("com");
        System.out.println(linked);
    }

}
