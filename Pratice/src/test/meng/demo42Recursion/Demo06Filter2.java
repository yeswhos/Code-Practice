package test.meng.demo42Recursion;

import java.io.File;
import java.io.FilenameFilter;

public class Demo06Filter2 {
    public static void getAllRecurseFile(File dir){
//        File [] arr = dir.listFiles(new FilenameFilter() {
//            @Override
//            public boolean accept(File acceptDir, String name) {
//                return new File(acceptDir, name).isDirectory() || name.toLowerCase().endsWith(".java");
//            }
//        });
        File [] arr = dir.listFiles((acceptDir, name)->new File(acceptDir, name).isDirectory() || name.toLowerCase().endsWith(".java"));
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
