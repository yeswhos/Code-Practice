package test.meng.demo47Net;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class FileTCPServer {
    public static void main(String[] args) throws IOException {
        ServerSocket server = new ServerSocket(8888);
        Socket socket = server.accept();
        InputStream is = socket.getInputStream();
        File file = new File("D:\\text");
        if(file != null){
            file.mkdirs();
        }
        byte [] bytes = new byte[1024];
        FileOutputStream fos = new FileOutputStream(file + "\\1.jpg");
        int len;
        while((len = is.read(bytes)) != -1){
            fos.write(bytes, 0, len);
        }
        socket.getOutputStream().write("上传成功".getBytes());
        is.close();
        socket.close();
        fos.close();
    }
}
