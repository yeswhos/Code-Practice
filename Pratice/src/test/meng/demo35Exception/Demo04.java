package test.meng.demo35Exception;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Demo04 {
    public static void main(String[] args)throws FileNotFoundException, IOException {
        readFile("c:\\a.txt");
    }
    // 对一个文件路径判断
    public static void readFile(String fileName) throws FileNotFoundException, IOException {
        if(!fileName.endsWith(".txt")){
            throw new IOException("后缀不对");
        }
        if(!fileName.equals("c:\\\\a.txt")){
            throw new FileNotFoundException("文件找不到");
        }
        System.out.println("文件到不到");
    }
}
