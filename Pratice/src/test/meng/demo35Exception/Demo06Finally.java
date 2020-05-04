package test.meng.demo35Exception;

import java.io.FileNotFoundException;
import java.io.IOException;

public class Demo06Finally {
    public static void readFile(String fileName) throws FileNotFoundException, IOException {
        if(!fileName.endsWith(".txt")){
            throw new IOException("后缀不对");
        }
        if(!fileName.equals("c:\\\\a.txt")){
            throw new FileNotFoundException("文件找不到");
        }
        System.out.println("路径没问题");
    }

    public static void main(String[] args) {
        try{
            readFile("c:\\a.txt");
        }catch (IOException e){
            e.printStackTrace();
        }finally {
            System.out.println("资源释放");
        }
    }
}
