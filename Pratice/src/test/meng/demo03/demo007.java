package test.meng.demo03;
import java.util.*;

public class demo007 {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        Demo008 stu = new Demo008();
        stu.setName("123");
        list.add(stu.getName());
        stu.setName("456");
        list.add(stu.getName());
        for(int i = 0; i < list.size(); i++){
            System.out.println(list.get(i));
        }
    }
}
