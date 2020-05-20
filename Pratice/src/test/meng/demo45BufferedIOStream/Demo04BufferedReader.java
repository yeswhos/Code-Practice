package test.meng.demo45BufferedIOStream;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Demo04BufferedReader {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\h.txt"));
        String str = null;
        while((str = br.readLine()) != null){
            System.out.println(str);
        }
        br.close();
    }
}
