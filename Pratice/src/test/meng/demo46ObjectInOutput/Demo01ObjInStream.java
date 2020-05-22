package test.meng.demo46ObjectInOutput;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class Demo01ObjInStream {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\j.txt"));
        Object o = ois.readObject();
        System.out.println(o);
        ois.close();
        Person p = (Person) o;
        System.out.println(p.getAge() + p.getName());
    }
}
