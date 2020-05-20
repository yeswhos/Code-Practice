package test.meng.demo45BufferedIOStream;

import java.io.*;
import java.util.HashMap;

public class Demo05Sort {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\sort.txt"));
        BufferedWriter bw = new BufferedWriter(new FileWriter("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\sortNew.txt"));
        HashMap<String, String> map = new HashMap<>();
        String line;
        while ((line = br.readLine()) != null){
            String [] str = line.split("\\.");
            map.put(str[0], str[1]);
        }
        for(String key : map.keySet()){
            String value = map.get(key);
            line = key + "." + value;
            bw.write(line);
            bw.newLine();
        }
        bw.close();
        br.close();
    }
}
