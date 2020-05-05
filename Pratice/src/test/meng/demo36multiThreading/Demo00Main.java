package test.meng.demo36multiThreading;

public class Demo00Main{
    public static void main(String[] args) {
        Thread mt = new Demo01();
        mt.start();
        for(int i = 0; i < 10; i++){
            System.out.println("main: " + i);
        }
    }
}
