package test.meng.demo25Collection;

import java.util.ArrayList;

public class Demo00CommonMethod {
    public static void main(String[] args) {
        ArrayList<String> coll = new ArrayList<>();
        coll.add("Fanhui");
        System.out.println("add()" + coll);

        coll.clear();
        System.out.println(coll);

        coll.add("Fanhui");
        System.out.println("remove()" + coll.remove("Fanhui"));
        System.out.println(coll);

        coll.add("Fanhui");
        System.out.println("contain()" + coll.contains("Fanhui"));

        System.out.println("isEmpty()" + coll.isEmpty());

        System.out.println("size()" + coll.size());

        Object [] array = coll.toArray();
        System.out.println("toArray" + array);
        for(int i = 0; i < array.length; i++){
            System.out.println(array[i]);
        }

    }

}
