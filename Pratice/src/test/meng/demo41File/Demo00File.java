package test.meng.demo41File;

import java.io.File;

public class Demo00File {
    public static void main(String[] args) {
        File f = new File("D:\\GitR\\COMP5920M-Scheduling");
        show00();
        show01("D:\\GitR\\COMP5920M-Scheduling\\", "Revision");
        show02(f, "Revision");

    }
    public static void show00(){
        File f1 = new File("D:\\GitR\\COMP5920M-Scheduling\\Revision");
        System.out.println(f1);
    }
    public static void show01(String parent, String child){
        File f1 = new File(parent, child);
        System.out.println(f1);
    }
    public static void show02(File parent, String child){
        File f2 = new File(parent, child);
        System.out.println(f2);
    }
}
