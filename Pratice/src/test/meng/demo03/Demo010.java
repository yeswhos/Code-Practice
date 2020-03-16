package test.meng.demo03;


import java.util.*;

public class Demo010 {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        Random r = new Random();
        for(int i = 0; i < 60; i++){
            int num = r.nextInt(100);
            list.add(num);
        }
        System.out.println(fliterNumber(list));
    }
    public static ArrayList<Integer> fliterNumber(ArrayList<Integer> list){
        ArrayList<Integer> list1 = new ArrayList<>();
        for(int i = 0; i < list.size(); i++){
            if(list.get(i) % 2 == 0){
                list1.add(list.get(i));
            }
        }
        return list1;
    }
}
