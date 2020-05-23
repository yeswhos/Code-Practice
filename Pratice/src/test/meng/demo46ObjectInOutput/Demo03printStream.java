package test.meng.demo46ObjectInOutput;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;

public class Demo03printStream {
    public static void main(String[] args) throws FileNotFoundException {
        PrintStream ps = new PrintStream(new FileOutputStream("C:\\Users\\yeswhos\\Desktop\\桌面不常用\\l.txt"));
        ps.write(97);
        ps.println(97);
        System.out.println("inside");
        System.setOut(ps);
        System.out.println("set out");
        ps.close();
    }
}
