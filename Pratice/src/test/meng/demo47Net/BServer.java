package test.meng.demo47Net;

import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class BServer {
    public static void main(String[] args) throws IOException {
        ServerSocket server = new ServerSocket(8080);
        Socket socket = server.accept();
        InputStream is = socket.getInputStream();
        int len;
        byte [] bytes = new byte[1024];
        while((len = is.read(bytes)) != -1){
            System.out.println(new String(bytes, 0, len));
        }
    }
}
