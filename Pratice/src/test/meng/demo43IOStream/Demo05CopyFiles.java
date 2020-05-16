package test.meng.demo43IOStream;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Demo05CopyFiles {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\1.jpg");
        FileInputStream fis = new FileInputStream("C:\\Users\\yeswhos\\Pictures\\Uplay\\Assassin's Creed® Odyssey\\Assassin's Creed® Odyssey2019-12-30-20-52-32.jpg");
        int len = 0;
        byte [] bytes = new byte[1024];
        while((len = fis.read(bytes)) != -1){
            fos.write(bytes, 0 ,len);
        }
        fos.close();
        fis.close();
    }
}
