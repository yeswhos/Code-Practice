package test.meng.demo36multiThreading;

public class Demo04setName {
    public static void main(String[] args) {
        Demo02Method mt = new Demo02Method();
        mt.setName("Fanhui");
        mt.start();

        new Demo02Method("Lulu").start();
    }
}
