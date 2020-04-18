package test.meng.demo21Date;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Demo01DateFormat {
    public static void demo00() throws ParseException {
        Date date = new Date();
        Date a = date;
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyy-MM-dd HH:mm:ss");
        String b = simpleDateFormat.format(a);
        Date c = simpleDateFormat.parse(b);
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);

    }

    public static void main(String[] args) throws ParseException {
        demo00();
    }
}
