package test.meng.demo28LinkedList;

import java.util.LinkedList;

public class Demo00 {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();
        list.add("1");
        list.add("2");
        list.add("3");
        list.add("4");
        list.add("5");
        addMethod(list);
        getMethod(list);
        removeMethod(list);
    }

    private static void addMethod(LinkedList<String> list){
        list.add("a");
        list.addFirst("first");
        list.push("popFirst");
        System.out.println(list);
    }
    private static void getMethod(LinkedList<String> list){
        String s1 = list.get(0);
        String s2 = list.getFirst();
        System.out.println("get" + s1 + s2);
    }
    private static void removeMethod(LinkedList<String> list){
        String s1 = list.remove(0);
        String s2 = list.removeFirst();
        String s3 = list.pop();
        System.out.println("remove" + s1 + "removeFirst" + s2 + "pop" + s3);
    }
}
