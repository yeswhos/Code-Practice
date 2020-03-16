package test.meng.demo03;
import java.util.*;

public class demo006 {
    public static void main(String[] args) {
        Random r = new Random();
/*        int a = r.nextInt(32) + 1;
        int b = r.nextInt(32) + 1;
        int c = r.nextInt(32) + 1;
        ArrayList<Integer> list = new ArrayList<>();
        list.add(a);
        list.add(b);
        list.add(c);*/
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i < 6; i++){
            int num = r.nextInt(33) + 1;
            list.add(num);
        }
        for(int i = 0; i < list.size(); i++){
            System.out.println(list.get(i));
        }
    }

}
