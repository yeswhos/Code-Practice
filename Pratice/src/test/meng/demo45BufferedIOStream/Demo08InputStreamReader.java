package test.meng.demo45BufferedIOStream;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Demo08InputStreamReader {
    public static void main(String[] args) throws IOException {
        InputStreamReader isr = new InputStreamReader(new FileInputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\i.txt"), "GBK");
        int len;
        while((len = isr.read()) != -1){
            System.out.println((char)len);
        }
        isr.close();
    }
}
