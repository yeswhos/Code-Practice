package test.meng.demo45BufferedIOStream;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Demo03BufferedWriter {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new FileWriter("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\h.txt"));
        for(int i =0; i < 10; i++){
            bw.write("Hello world");
            bw.newLine();
        }
        bw.flush();
        bw.close();

    }
}
