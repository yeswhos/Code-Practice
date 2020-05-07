package test.meng.demo36multiThreading;

public class Demo09Security implements Runnable{
    private int ticket = 100;
    @Override
    public void run() {
        while(ticket > 0){
            System.out.println("线程" + Thread.currentThread().getName() + "--->第" + ticket);
            ticket--;
        }

    }
}
