package test.meng.demo43IOStream;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Demo04MultiInputStream {
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\a.txt");
        //一次读两个字符，【】起到缓冲作用
//        byte [] bytes = new byte[2];
//        int len = fis.read(bytes);
//        System.out.println(len);
//        System.out.println(Arrays.toString(bytes));
//        System.out.println(new String(bytes));

//        -------------------------------------------------------
        byte [] bytes1 = new byte[1024];
        int len = 0;
        while((len = fis.read(bytes1)) != -1){
            System.out.println(new String(bytes1, 0, 12));
        }
        fis.close();
    }
}
