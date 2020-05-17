package test.meng.demo43IOStream;

import java.io.*;

public class Demo11TFileryCatchSimplify {
    public static void main(String[] args) throws FileNotFoundException {
        FileOutputStream fos = new FileOutputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\1.jpg");
        FileInputStream fis = new FileInputStream("C:\\Users\\yeswhos\\Pictures\\Uplay\\Assassin's Creed® Odyssey\\Assassin's Creed® Odyssey2019-12-30-20-52-32.jpg");
        try(fis; fos){
            int len = 0;
            byte [] bytes = new byte[1024];
            while((len = fis.read(bytes)) != -1){
                fos.write(bytes, 0 ,len);
            }
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
