package test.meng.demo45BufferedIOStream;

import java.io.*;

public class Demo02BufferedCopyFile {
    public static void main(String[] args) throws IOException {
        BufferedInputStream bis = new BufferedInputStream(new FileInputStream("C:\\Users\\yeswhos\\Pictures\\Uplay\\Tom Clancy's Rainbow Six® Siege\\Tom Clancy's Rainbow Six® Siege2020-4-5-21-1-57.jpg"));
        BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\buffered.jpg"));
        int len = 0;
        while((len = bis.read()) != -1){
            bos.write(len);
        }
        bis.close();
        bos.close();
    }
}
