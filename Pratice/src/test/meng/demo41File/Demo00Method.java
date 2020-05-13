package test.meng.demo41File;

import java.io.File;

public class Demo00Method {
    public static void main(String[] args) {
        show00();
        show01();
        show02();
        show03();
    }
    private static void show00(){
        File f1 = new File("D:\\GitR\\COMP5920M-Scheduling\\Revision\\Scheduling.xmind");
        String absolutePath = f1.getAbsolutePath();
        System.out.println(absolutePath);
        File f2 = new File("Scheduling.xmind");
        String ab = f2.getAbsolutePath();
        System.out.println(ab);
    }
    private static void show01(){
        File f1 = new File("D:\\GitR\\COMP5920M-Scheduling\\Revision\\Scheduling.xmind");
        String absolutePath = f1.getPath();
        System.out.println(absolutePath);
        File f2 = new File("Scheduling.xmind");
        String ab = f2.getPath();
        System.out.println(ab);
    }
    private static void show02(){
        File f1 = new File("D:\\GitR\\COMP5920M-Scheduling\\Revision\\Scheduling.xmind");
        String absolutePath = f1.getName();
        System.out.println(absolutePath);
    }
    private static void show03(){
        File f1 = new File("D:\\GitR\\COMP5920M-Scheduling\\Revision\\Scheduling.xmind");
        long a = f1.length();
        System.out.println(a);
    }
}
