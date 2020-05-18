package test.meng.demo44Properties;

import java.util.Properties;
import java.util.Set;

public class Demo00PropertyMethod {
    public static void main(String[] args) {
        show();
    }
    public static void show(){
        Properties prop = new Properties();
        prop.setProperty("Fanhui", "23");
        prop.setProperty("Lulu", "22");
        Set<String> set = prop.stringPropertyNames();
        for(String str : set){
            String value = prop.getProperty(str);
            System.out.println(str + value);
        }
    }
}
