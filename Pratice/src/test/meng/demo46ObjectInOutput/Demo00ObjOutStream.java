package test.meng.demo46ObjectInOutput;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class Demo00ObjOutStream {
    public static void main(String[] args) throws IOException {
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\j.txt"));
        oos.writeObject(new Person("Fanhui", 22));
        oos.close();
    }
}
