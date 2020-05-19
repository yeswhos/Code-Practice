package test.meng.demo45BufferedIOStream;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;

public class Demo01BufferedInputStream {
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\g.txt");
        BufferedInputStream bis = new BufferedInputStream(fis);
        int len = 0;
//
//        while((len = bis.read()) != -1){
//            System.out.print((char)len);
//        }

        //---------------------------------------------

        byte [] bytes = new byte[1024];
        while((len = bis.read(bytes)) != -1){
            System.out.println(new String(bytes, 0, len));
        }
        bis.close();
    }
}
