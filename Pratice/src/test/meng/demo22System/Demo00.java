package test.meng.demo22System;

public class Demo00 {
    public static void main(String[] args) {
        /*
        system.currenttimemills
         */
        double a = System.currentTimeMillis();
        for(int i = 0; i < 99999; i++){
            System.out.println(i);
        }
        double b = System.currentTimeMillis();
        System.out.println(b - a);

        /*
        arraycopy
         */
        int [] c = {1, 2, 3, 4, 5};
        int [] d = {6, 7, 8, 9, 10};
        System.arraycopy(c, 0, d, 0, 4);
        for(int i = 0; i < d.length; i++)
            System.out.println(d[i]);

    }
}
