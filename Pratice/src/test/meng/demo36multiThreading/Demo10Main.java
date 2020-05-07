package test.meng.demo36multiThreading;

public class Demo10Main {
    public static void main(String[] args) {
        Demo09Security run = new Demo09Security();
        Thread t0 = new Thread(run);
        Thread t1 = new Thread(run);
        Thread t2 = new Thread(run);
        t0.start();
        t1.start();
        t2.start();
    }
}
