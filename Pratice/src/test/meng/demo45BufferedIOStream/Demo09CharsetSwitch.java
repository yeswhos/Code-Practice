package test.meng.demo45BufferedIOStream;

import java.io.*;

public class Demo09CharsetSwitch {
    public static void main(String[] args) throws IOException {
        InputStreamReader isr = new InputStreamReader(new FileInputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\i.txt"), "UTF-8");
        OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\i_charset.txt"), "GBK");
        int len;
        while((len = isr.read()) != -1){
            osw.write(len);
        }
        osw.flush();
        isr.close();

        osw.close();
    }
}
