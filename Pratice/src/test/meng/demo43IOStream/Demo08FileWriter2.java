package test.meng.demo43IOStream;

import java.io.FileWriter;
import java.io.IOException;

public class Demo08FileWriter2 {
    public static void main(String[] args) throws IOException {
        FileWriter fw = new FileWriter("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\e.txt");
        char [] cs = {'a', 'b', 'c'};
        fw.write(cs, 0, 3);
        fw.flush();
        String str = "123456";
        fw.write(str, 0, 4);
        fw.flush();
        fw.close();
    }
}
