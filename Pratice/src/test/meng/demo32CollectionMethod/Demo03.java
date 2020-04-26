package test.meng.demo32CollectionMethod;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Demo03 {
    public static void main(String[] args) {
        Demo02Person p1 = new Demo02Person(23, "Fanhui");
        Demo02Person p2 = new Demo02Person(21, "Lulu");
        Demo02Person p3 = new Demo02Person(23, "Lulu");
        ArrayList<Demo02Person> list02 = new ArrayList<>();
        Collections.addAll(list02, p1, p2, p3);
        Collections.sort(list02, new Comparator<Demo02Person>() {
            @Override
            public int compare(Demo02Person o1, Demo02Person o2) {
                int result = o1.getAge() - o2.getAge();
                if(o1.getAge() == o2.getAge()){
                    result = o1.getName().charAt(0) - o2.getName().charAt(0);
                }
                return result;
            }
        });
        System.out.println(list02);
    }
}
