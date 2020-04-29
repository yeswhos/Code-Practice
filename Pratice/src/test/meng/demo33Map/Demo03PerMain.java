package test.meng.demo33Map;

import java.util.*;

public class Demo03PerMain {
    public static void main(String[] args) {
//        method00();
        method01();
    }
    public static void method00(){
        HashMap<Integer, Person> map = new HashMap();
        map.put(1, new Person("Fanhui", 23));
        map.put(2, new Person("Lulu", 23));
        map.put(3, new Person("Fanhui", 21));
        map.put(3, new Person("Nobody", 18));
        Set<Integer> set = map.keySet();
        for(Integer i : set){
            Person value = map.get(i);
            System.out.println(value);
        }
    }

    public static void method01(){
        HashMap<Person, Integer> map = new HashMap<>();
        map.put(new Person("Fanhui", 23), 1);
        map.put(new Person("Lulu", 23), 2);
        map.put(new Person("Fanhui", 21), 3);
        map.put(new Person("Nobody", 18), 3);
        Set<Map.Entry<Person, Integer>> set = map.entrySet();
        for(Map.Entry<Person, Integer> set1 : set){
            Person a = set1.getKey();
            Integer b = set1.getValue();
            System.out.println(a);
            System.out.println(b);
        }

    }
}
