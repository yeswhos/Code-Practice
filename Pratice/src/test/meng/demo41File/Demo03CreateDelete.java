package test.meng.demo41File;

import java.io.File;

public class Demo03CreateDelete{
    public static void show00() throws Exception{
        File f1 = new File("C:\\Users\\yeswhos\\Desktop\\a.txt");
        boolean a = f1.createNewFile();
        System.out.println("a: " + a);
    }
    public static void  show01(){
        File f1 = new File("C:\\Users\\yeswhos\\Desktop\\test");
        System.out.println(f1.mkdir());
        File f2 = new File("C:\\Users\\yeswhos\\Desktop\\test\\d1\\d2");
        System.out.println(f2.mkdirs());
    }
    public static void  show02(){
        File f1 = new File("C:\\Users\\yeswhos\\Desktop\\test\\d1\\d2");
        System.out.println(f1.delete());
    }

    public static void main(String[] args) throws Exception {
//        show00();
//        show01();
        show02();
    }
}
