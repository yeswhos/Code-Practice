package test.meng.demo14Final;

public class Demo01 {
    public static void main(String[] args) {
        Demo00 demo00 = new Demo00();
        System.out.println(demo00.name);
        System.out.println(demo00.getName());
        demo00 = new Demo00("Meng");
        System.out.println(demo00.getName());
    }
}
