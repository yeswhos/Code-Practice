package test.meng.demo35Exception;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Demo00 {
    public static void main(String[] args) /*throws ParseException */{
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
        Date date = null;
        try{
            date = sdf.parse("2020-05-20");
        }catch (ParseException e){
            e.printStackTrace();
        }
        System.out.println(date);

        int [] arr = {1, 2, 3};
        try{
            int a = arr[4];
        }catch (RuntimeException e){
            e.printStackTrace();
        }
        System.out.println("continue");
    }
}
