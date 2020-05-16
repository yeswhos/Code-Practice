package test.meng.demo43IOStream;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class Demo00OutputStream {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream("C:\\Users\\yeswhos\\Desktop\\a.txt");
        fos.write(97);
        fos.close();
    }
}
