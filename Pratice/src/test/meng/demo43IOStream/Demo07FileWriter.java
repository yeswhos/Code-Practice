package test.meng.demo43IOStream;

import java.io.FileWriter;
import java.io.IOException;

public class Demo07FileWriter {
    public static void main(String[] args) throws IOException {
        FileWriter fw = new FileWriter("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\c.txt");
        fw.write(97);
        fw.flush();
        fw.close();
    }
}
