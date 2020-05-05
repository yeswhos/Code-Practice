package test.meng.demo36multiThreading;

public class Demo01 extends Thread{
    @Override
    public void run(){
        for(int i = 0; i < 10; i++){
            System.out.println("run" + i);
        }
    }
}
