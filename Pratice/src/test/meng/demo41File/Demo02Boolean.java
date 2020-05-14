package test.meng.demo41File;

import java.io.File;

public class Demo02Boolean {
    public static void main(String[] args) {
        show00();
        show01();
    }
    public static void show00(){
        File f1 = new File("D:\\GitR\\Code-Practice");
        System.out.println(f1.exists());
        File f2 = new File("README.md");
        System.out.println(f2.exists());
    }
    public static void show01(){
        File f1 = new File("D:\\GitR\\Code-Practice");
        File f2 = new File("D:\\GitR\\Code-Practice\\README.md");
        if(f1.exists()){
            System.out.println(f1.isDirectory());
            System.out.println(f1.isFile());
        }
        System.out.println("======================================");
        if(f2.exists()){
            System.out.println(f2.isDirectory());
            System.out.println(f2.isFile());
        }
    }
}
