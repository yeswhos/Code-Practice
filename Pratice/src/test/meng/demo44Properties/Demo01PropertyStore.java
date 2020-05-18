package test.meng.demo44Properties;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Properties;

public class Demo01PropertyStore {
    public static void main(String[] args) throws IOException {
        show();
    }
    public static void show() throws IOException {
        Properties prop = new Properties();
        prop.setProperty("Fanhui", "23");
        prop.setProperty("Lulu", "22");
        FileWriter fw = new FileWriter("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\f.txt");
        prop.store(fw, "05.18");
        fw.close();
    }
}
