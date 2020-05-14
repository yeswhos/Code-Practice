package test.meng.demo42Recursion;

import java.io.File;

public class Demo04Java {
    public static void getAllRecurseFile(File dir){
        File [] arr = dir.listFiles();
        for(File f : arr){
            String s = f.toString();
            if(f.isDirectory()){
                System.out.println(f);
            }
            else{
                if(f.toString().toLowerCase().endsWith(".java")){
                    System.out.println(f);
                }
            }
        }
    }

    public static void main(String[] args) {
        File f = new File("C:\\Users\\yeswhos\\Desktop\\桌面不常用");
        getAllRecurseFile(f);
    }
}
