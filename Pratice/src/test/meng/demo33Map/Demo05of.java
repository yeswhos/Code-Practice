package test.meng.demo33Map;

import java.util.List;
import java.util.Map;
import java.util.Set;

public class Demo05of {
    public static void main(String[] args) {
        List<Integer> list = List.of(1, 2, 3, 4, 5);
//        list.add(1);
        System.out.println(list);

        Set<Integer> set = Set.of(1, 2, 3, 4, 5, 6);
        System.out.println(set);

        Map<Integer, String> map = Map.of(1,"1", 2, "2" );
        System.out.println(map);
    }
}
