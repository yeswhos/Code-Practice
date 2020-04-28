package test.meng.demo33Map;

import java.util.HashMap;
import java.util.Map;

public class Demo00Map0 {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<>();
        String s1 = map.put("Fanhui", "Lulu1");
        System.out.println(s1);
        String s2 = map.put("Fanhui", "Lulu2");
        System.out.println(s2);
        System.out.println("-----------------------");

//        String s3 = map.remove("Fanhui");
//        System.out.println(s3);
        System.out.println("-----------------------");
        String s4 = map.get("Fanhui");
        System.out.println(s4);
        System.out.println("-----------------------");
        boolean b1 = map.containsKey("Fanhui");
        System.out.println(b1);
        System.out.println(map);
    }
}
