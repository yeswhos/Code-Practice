package test.meng.demo47Net;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;

public class FileTCPServer {
    public static void main(String[] args) throws IOException {
        ServerSocket server = new ServerSocket(8888);
        while(true){
            Socket socket = server.accept();
            new Thread(new Runnable() {
                @Override
                public void run() {
                    try{
                        InputStream is = socket.getInputStream();
                        File file = new File("D:\\text");
                        if(file != null){
                            file.mkdirs();
                        }
                        String filename = "meng" + System.currentTimeMillis() + new Random().nextInt(9999) + ".jpg";
                        byte [] bytes = new byte[1024];
                        //        FileOutputStream fos = new FileOutputStream(file + "\\1.jpg");
                        FileOutputStream fos = new FileOutputStream(file + "\\" + filename);
                        int len;
                        while((len = is.read(bytes)) != -1){
                            fos.write(bytes, 0, len);
                        }
                        socket.getOutputStream().write("上传成功".getBytes());
                        is.close();
                        socket.close();
                        fos.close();
                    }catch (IOException e){
                        e.printStackTrace();
                    }

                }
            }).start();

        }

    }
}
