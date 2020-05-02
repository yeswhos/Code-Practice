package test.meng.demo35Exception;

import java.io.FileNotFoundException;
import java.io.IOException;

public class Demo05tryCatch {
    public static void readFile(String fileName) throws FileNotFoundException, IOException {
        if(!fileName.endsWith(".txt")){
            throw new IOException("后缀不对");
        }
        if(!fileName.equals("c:\\\\a.txt")){
            throw new FileNotFoundException("文件找不到");
        }
        System.out.println("路径没问题");
    }

    public static void main(String[] args) throws IOException{
        try{
            readFile("c:\\\\a.txt");
        }catch (IOException e){
            System.out.println("catch - 后缀不是.txt");
        }
        System.out.println("出了问题，还能继续");
    }
}
