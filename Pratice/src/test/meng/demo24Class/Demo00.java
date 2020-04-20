package test.meng.demo24Class;

public class Demo00 {
    public static void main(String[] args) {
        Integer int1 = new Integer(1);
        System.out.println(int1);
        Integer int2 = new Integer("2");
        System.out.println(int2);
        Integer int3 = Integer.valueOf(3);
        System.out.println(int3);
        Integer int4 = Integer.valueOf("4");
        System.out.println(int4);
        int int5 = int1.intValue();
        System.out.println(int5);
    }
}
