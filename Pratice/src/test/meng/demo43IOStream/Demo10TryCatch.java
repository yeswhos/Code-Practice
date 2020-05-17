package test.meng.demo43IOStream;

import java.io.FileWriter;
import java.io.IOException;

public class Demo10TryCatch {
    public static void main(String[] args) {
        FileWriter fw = null;
        try{
            fw = new FileWriter("D:\\Users\\yeswhos\\Desktop\\桌面不常用\\e.txt", true);
            for(int i = 0; i < 5; i++) {
                fw.write("Hello World");
                fw.write("\r\n");
            }
        }catch (IOException e){
            e.printStackTrace();
        }finally {
            if(fw != null){
                try{
                    fw.close();
                }catch (IOException e){
                    e.printStackTrace();
                }
            }

        }

    }
}
