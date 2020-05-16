package test.meng.demo43IOStream;

import java.io.FileOutputStream;
import java.io.IOException;

public class Demo01MultiOutputStream {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream("C:\\Users\\yeswhos\\Desktop\\b.txt");
//        fos.write(49);
//        fos.write(48);
//        fos.write(48);

//        byte [] bytes = {49, 48, 48};
//        fos.write(bytes);
//        fos.write(bytes, 1, 2);

        byte [] bytes = "你好".getBytes();
        fos.write(bytes);
        fos.close();

    }
}
