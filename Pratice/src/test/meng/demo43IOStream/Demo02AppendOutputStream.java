package test.meng.demo43IOStream;

import java.io.FileOutputStream;
import java.io.IOException;

public class Demo02AppendOutputStream {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream("C:\\Users\\yeswhos\\Desktop\\b.txt", true);
        for(int i = 0; i < 10; i++){
            fos.write("你好".getBytes());
            fos.write("\r\n".getBytes());
        }
        fos.close();
    }
}
