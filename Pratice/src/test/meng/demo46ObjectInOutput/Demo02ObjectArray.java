package test.meng.demo46ObjectInOutput;

import java.io.*;
import java.util.ArrayList;

public class Demo02ObjectArray {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        ArrayList<Person> list1 = new ArrayList<>();
        list1.add(new Person("Fanhui", 22));
        list1.add(new Person("Lulu", 22));
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\k.txt"));
        oos.writeObject(list1);
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\k.txt"));
        Object o = ois.readObject();
        ArrayList<Person> list2 = (ArrayList<Person>) o;
        for(Person p : list2){
            System.out.println(p);
        }
        ois.close();
        oos.close();
    }
}
