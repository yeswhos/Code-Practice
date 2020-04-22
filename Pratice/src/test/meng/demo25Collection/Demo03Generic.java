package test.meng.demo25Collection;

import java.util.ArrayList;
import java.util.Iterator;

public class Demo03Generic {
    public static void main(String[] args) {
        demo00();
        demo01();
    }
    //不使用泛型
    private static void demo00(){

        ArrayList list = new ArrayList();
        list.add("abc");
        list.add(1);
        Iterator it = list.iterator();
        while(it.hasNext()){
            Object obj = it.next();
            System.out.println("不用泛型：" + obj);
//            String s = (String)obj;
//            System.out.println("汤加可乐法力无边，转换string会出错：" + s);
        }
    }
    //用泛型
    private static void demo01(){
        ArrayList<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        Iterator<Integer> it = list.iterator();
        while(it.hasNext()){
            Integer a = it.next();
            System.out.println("用泛型:" + a);
        }
    }
}
