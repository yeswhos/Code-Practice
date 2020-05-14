package test.meng.demo41File;

import java.io.File;

public class Demo04Iteration {
    public static void show00(){
        File f1 = new File("C:\\Users\\yeswhos\\Desktop\\桌面不常用");
        String [] arr = f1.list();
        for(String s : arr){
            System.out.println(s);
        }
    }
    public static void show01(){
        File f1 = new File("C:\\Users\\yeswhos\\Desktop\\桌面不常用");
        File [] f2 = f1.listFiles();
        for(File f : f2){
            System.out.println(f);
        }
    }

    public static void main(String[] args) {
//        show00();
        show01();
    }
}
