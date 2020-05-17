package test.meng.demo43IOStream;

import java.io.FileWriter;
import java.io.IOException;

public class Demo09Writer3{
    public static void main(String[] args) throws IOException {
        FileWriter fw = new FileWriter("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\e.txt", true);
        for(int i = 0; i < 5; i++){
            fw.write("Hello World");
            fw.write("\r\n");
        }
        fw.close();
    }
}
