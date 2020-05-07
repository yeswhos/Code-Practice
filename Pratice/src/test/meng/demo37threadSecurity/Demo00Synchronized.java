package test.meng.demo37threadSecurity;

public class Demo00Synchronized implements Runnable{
    private int ticket = 100;
    Object obj = new Object();
    @Override
    public void run() {
        synchronized (obj){
            while(ticket > 0){
                System.out.println("线程" + Thread.currentThread().getName() + "--->第" + ticket);
                ticket--;
            }
        }
    }
}
