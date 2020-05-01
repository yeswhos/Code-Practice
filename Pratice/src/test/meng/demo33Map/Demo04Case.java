package test.meng.demo33Map;

import java.util.HashMap;
import java.util.Scanner;

/*
    统计字符换次数
 */
public class Demo04Case {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("please input string");
        String str = sc.next();
        count(str);
    }
    public static void count(String str){
        HashMap<Character, Integer> map = new HashMap<>();
        for(Character c : str.toCharArray()){
            if(map.containsKey(c)){
                Integer value = map.get(c);
                value++;
                map.put(c, value);
            }else{
                map.put(c, 1);
            }
        }
        for(Character c : map.keySet()){
            Integer value = map.get(c);
            System.out.println("string: %d" + c + " has appeared " + value + "times");
        }
    }
}
