package test.meng.demo33Map;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class Demo01MapTraverse {
    public static void main(String[] args) {
        Map<Integer, String> map = new HashMap<>();
        map.put(0, "Yasuo");
        map.put(1, "Draven");
        Set<Integer> set = map.keySet();
        Iterator<Integer> it = set.iterator();
        while(it.hasNext()){
            int i = it.next();
//            System.out.println(i);
            String s = map.get(i);
            System.out.println(s);
        }
        System.out.println("------------------------");
        for(Integer i : set){
            String s = map.get(i);
            System.out.println(s);
        }
    }
}
