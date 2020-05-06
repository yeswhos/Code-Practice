package test.meng.demo36multiThreading;

public class Demo02Method extends Thread{
    @Override
    public void run(){
//        String name = getName();
//        System.out.println(name);
        System.out.println(Thread.currentThread().getName());
    }

    public Demo02Method() {
    }

    public Demo02Method(String name) {
        super(name);
    }
}
