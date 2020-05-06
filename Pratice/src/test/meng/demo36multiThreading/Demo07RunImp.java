package test.meng.demo36multiThreading;

public class Demo07RunImp implements Runnable{
    @Override
    public void run(){
        for(int i  = 0; i < 20; i++){
            System.out.println(Thread.currentThread().getName() + "---" + i);
        }
    }
}
