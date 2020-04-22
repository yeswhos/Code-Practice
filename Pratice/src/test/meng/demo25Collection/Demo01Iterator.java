package test.meng.demo25Collection;

import java.util.ArrayList;
import java.util.Iterator;

public class Demo01Iterator {
    public static void main(String[] args) {
        ArrayList<Integer> coll = new ArrayList<>();
        for(int i = 0; i < 5; i++){
            coll.add(i);
        }
        Iterator<Integer> iterator1 = coll.iterator();
        while(iterator1.hasNext()){
            int a = iterator1.next();
            System.out.println(a);
        }

        for(Iterator<Integer> iterator2 = coll.iterator(); iterator2.hasNext();){
            int b = iterator2.next();
            System.out.println(b);
        }

    }
}
