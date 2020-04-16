package test.meng.demo20Object;

public class Demo01 {
    public static void main(String[] args) {
        Demo00 demo00 = new Demo00("Yasuo", 33);
        Demo00 demo01 = new Demo00("Draven", 23);
        System.out.println(demo00);
        System.out.println(demo01);
        System.out.println(demo00.equals(demo01));

    }
}
