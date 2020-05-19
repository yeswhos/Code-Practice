package test.meng.demo45BufferedIOStream;

import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Demo00BufferedOutputStream {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\g.txt");
        BufferedOutputStream bof = new BufferedOutputStream(fos);
        bof.write("BufferedOutputStream test".getBytes());
        bof.flush();
        //不用关fos
        bof.close();
    }
}
