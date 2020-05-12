package test.meng.demo40ThreadAndLambda;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Comparator;

public class Demo05Lambda02 {
    public static void main(String[] args) {
        Person arr[] = {
                new Person(22, "Fanhui"),
                new Person(23, "Lulu")
        };
        Arrays.sort(arr, new Comparator<Person>() {
            @Override
            public int compare(Person o1, Person o2) {
                return o1.getAge() - o2.getAge();
            }
        });
        for(Person p : arr){
            System.out.println(p);
        }
        System.out.println("---------------");

        Arrays.sort(arr, (Person o1, Person o2)-> {
            return o2.getAge() - o1.getAge();
        });
        for(Person p : arr){
            System.out.println(p);
        }
    }
}
