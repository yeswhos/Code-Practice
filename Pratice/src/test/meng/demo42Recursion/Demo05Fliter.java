package test.meng.demo42Recursion;

import java.io.File;
import java.io.FileFilter;

public class Demo05Fliter {
    public static void getAllRecurseFile(File dir){
//        File [] arr = dir.listFiles(new FileFilterD());
        //---------------------------------------------
//        File [] arr = dir.listFiles(new FileFilter() {
//            @Override
//            public boolean accept(File pathname) {
//                return pathname.isDirectory() || pathname.toString().toLowerCase().endsWith(".java");
//            }
//        });
        //-------------------------------------------------
//        File [] arr = dir.listFiles((File pathname)->{
//            return pathname.isDirectory() || pathname.toString().toLowerCase().endsWith(".java");
//        });
//        -------------------------------------------------------
        File [] arr = dir.listFiles((pathname)-> pathname.isDirectory() || pathname.toString().toLowerCase().endsWith(".java"));
        for(File f : arr){
            //String s = f.toString();
            if(f.isDirectory()){
                getAllRecurseFile(f);
            }
            else{
                System.out.println(f);
            }
        }
    }

    public static void main(String[] args) {
        File f = new File("C:\\Users\\yeswhos\\Desktop\\桌面不常用");
        getAllRecurseFile(f);
    }
}


