package test.meng.demo43IOStream;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Demo06FileReader {
    public static void main(String[] args) throws IOException {
        FileReader fr = new FileReader("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\b.txt");
        int len = 0;
//        while((len = fr.read()) != -1){
//            System.out.println((char)len);
//        }
        System.out.println("-----------------------------------");
        char [] c = new char[1024];
        while((len = fr.read(c)) != -1){
//            System.out.println(c);
            System.out.println(new String(c, 0, 14));
        }
        fr.close();
    }
}
