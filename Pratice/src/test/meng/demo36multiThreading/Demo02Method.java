package test.meng.demo36multiThreading;

public class Demo02Method extends Thread{
    @Override
    public void run(){
//        String name = getName();
//        System.out.println(name);
        System.out.println(Thread.currentThread().getName());
    }
}
