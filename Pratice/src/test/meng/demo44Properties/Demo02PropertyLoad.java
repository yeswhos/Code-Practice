package test.meng.demo44Properties;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Properties;
import java.util.Set;

public class Demo02PropertyLoad {
    public static void show() throws IOException {
        Properties prop = new Properties();
        prop.setProperty("Fanhui", "23");
        prop.setProperty("Lulu", "22");
        FileReader fr = new FileReader("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\f.txt");
        prop.load(fr);
        Set<String> set = prop.stringPropertyNames();
        for(String str : set){
            String value = prop.getProperty(str);
            System.out.println(value + "=" + str);
        }
        fr.close();
    }

    public static void main(String[] args) throws IOException{
        show();
    }
}
