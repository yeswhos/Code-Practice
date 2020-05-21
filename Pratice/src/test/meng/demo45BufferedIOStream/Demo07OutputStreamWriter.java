package test.meng.demo45BufferedIOStream;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Demo07OutputStreamWriter {
    public static void main(String[] args) throws IOException {
        OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\i.txt"), "UTF-8");
        osw.write("你好");
        osw.flush();
        osw.close();
    }
}
