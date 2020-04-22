package test.meng.demo25Collection;

import java.util.ArrayList;
import java.util.Iterator;

public class Demo12Generic {
    public static void main(String[] args) {
        ArrayList<Integer> list1 = new ArrayList<>();
        list1.add(1);
        list1.add(2);
        printArray(list1);
    }

    public static void printArray(ArrayList<?> list){
        Iterator<?> it = list.iterator();
        while(it.hasNext()){
            Object obj = it.next();
            System.out.println(obj);
        }
    }
}
