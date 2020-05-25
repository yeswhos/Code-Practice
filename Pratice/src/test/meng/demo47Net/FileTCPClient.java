package test.meng.demo47Net;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class FileTCPClient {
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\1.jpg");
        Socket socket = new Socket("127.0.0.1", 8888);
        OutputStream os = socket.getOutputStream();
        byte [] bytes = new byte[1024];
        int len;
        while((len = fis.read(bytes)) != -1){
            os.write(bytes, 0, len);
        }
        InputStream is = socket.getInputStream();
        while ((len = is.read(bytes)) != -1){
            System.out.println(new String(bytes, 0, len));
        }
        fis.close();
        socket.close();
        os.close();
    }
}
