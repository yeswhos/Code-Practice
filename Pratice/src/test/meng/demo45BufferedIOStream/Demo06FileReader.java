package test.meng.demo45BufferedIOStream;

import java.io.FileReader;
import java.io.IOException;

public class Demo06FileReader {
    public static void main(String[] args) throws IOException {
        FileReader fr = new FileReader("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\test.txt");
        int len;
        while((len = fr.read()) != -1){
//            System.out.println(len);
            System.out.println((char)len);
        }
        fr.close();
    }
}
