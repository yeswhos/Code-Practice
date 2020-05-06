package test.meng.demo36multiThreading;

public class Demo06Runnable {
    public static void main(String[] args) {
        Demo07RunImp run = new Demo07RunImp();
        Thread mt = new Thread(run);
        mt.start();
        for(int i  = 0; i < 20; i++){
            System.out.println("main: " + Thread.currentThread().getName() + "---" + i);
        }
    }
}
