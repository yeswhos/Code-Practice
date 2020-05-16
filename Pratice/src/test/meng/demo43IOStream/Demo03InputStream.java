package test.meng.demo43IOStream;

import java.io.FileInputStream;
import java.io.IOException;

public class Demo03InputStream{
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\a.txt");
//        int len = fis.read();
//        System.out.println((char)len);
        int len = 0;
        while((len = fis.read()) != -1){
//            len = fis.read();
            System.out.println((char)len);
        }
        fis.close();
    }
}
