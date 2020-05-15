package test.meng.demo42Recursion;

import java.io.File;
import java.util.logging.Filter;

public class FileFilterD implements java.io.FileFilter {
    @Override
    public boolean accept(File pathname) {
        String s = pathname.toString();
        if(pathname.isDirectory()){
            return true;
        }
        if(s.endsWith(".java")){
            return true;
        }
        else{
            return false;
        }
    }
}
