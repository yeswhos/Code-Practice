package test.meng.demo29Set;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class Demo00 {
    public static void main(String[] args) {
        Set<Integer> set = new HashSet<>();
        set.add(1);
        set.add(2);
        set.add(3);
        set.add(1);
        for(Integer i : set){
            System.out.println(i);
        }

        Iterator<Integer> it = set.iterator();
        while(it.hasNext()){
            System.out.println(it.next());
        }
    }
}
