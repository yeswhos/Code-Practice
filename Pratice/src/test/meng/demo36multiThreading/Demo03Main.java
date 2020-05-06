package test.meng.demo36multiThreading;

public class Demo03Main {
    public static void main(String[] args) {
        Thread mt = new Demo02Method();
        mt.start();
        new Demo02Method().start();
        new Demo02Method().start();
        System.out.println(Thread.currentThread().getName());
    }
}
