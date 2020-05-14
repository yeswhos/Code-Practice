package test.meng.demo42Recursion;

import java.io.File;

public class Demo03Files {
    public static void getAllFile(File dir){
        File [] arr = dir.listFiles();
        for(File f : arr){
            System.out.println(f);
        }
    }
    public static void getAllRecurseFile(File dir){
        File [] arr = dir.listFiles();
        for(File f : arr){
            if(f.isDirectory()){
                System.out.println(f);
                getAllRecurseFile(f);
            }
            else{
                System.out.println(f);
            }
        }
    }

    public static void main(String[] args) {
        File f = new File("C:\\Users\\yeswhos\\Desktop\\桌面不常用");
//        getAllFile(f);
        getAllRecurseFile(f);
    }
}
