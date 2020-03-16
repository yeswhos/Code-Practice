package test.meng.demo03;

import java.util.ArrayList;

public class Demo009 {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("123");
        list.add("456");
        list.add("789");
        printList(list);
    }
    public static void printList(ArrayList<String> list){
        for(int i = 0; i < list.size(); i++){
            System.out.println(list.get(i));
        }
    }
}
