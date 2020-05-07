package test.meng.demo37threadSecurity;

public class Demo02SynMethod implements Runnable{
    private static int ticket = 100;
    Object obj = new Object();
    @Override
    public void run() {
        while(true){
            payTicket();
        }
    }
//    public synchronized void payTicket(){
//        if(ticket > 0){
//            System.out.println("线程" + Thread.currentThread().getName() + "--->第" + ticket);
//            ticket--;
//        }
//    }

    public static synchronized void payTicket(){
        if(ticket > 0){
            System.out.println("线程" + Thread.currentThread().getName() + "--->第" + ticket);
            ticket--;
        }
    }
}
