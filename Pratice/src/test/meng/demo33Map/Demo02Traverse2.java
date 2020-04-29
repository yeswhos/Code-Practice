package test.meng.demo33Map;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class Demo02Traverse2 {
    public static void main(String[] args) {
        Map<Integer, String> map = new HashMap<>();
        map.put(1, "Fanhui");
        map.put(2, "Lulu");
        Set<Map.Entry<Integer, String>> set = map.entrySet();
        Iterator<Map.Entry<Integer, String>> it = set.iterator();
        while(it.hasNext()){
            Map.Entry<Integer, String> entry = it.next();
            Integer a = entry.getKey();
            String b = entry.getValue();
            System.out.println(a + " and " + b);
        }

        System.out.println("------------------------------");

        for(Map.Entry<Integer, String> map1 : set){
            Integer a = map1.getKey();
            String b = map1.getValue();
            System.out.printf(a + " and " + b);
        }
    }
}
