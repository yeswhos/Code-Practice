package test.meng.demo37threadSecurity;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Demo03Lock implements Runnable{
    private static int ticket = 100;
    Object obj = new Object();
    Lock l = new ReentrantLock();
//    @Override
//    public void run() {
//
//        while(true){
//            l.lock();
//            payTicket();
//            l.unlock();
//        }
//    }
    //第二中方法，
    @Override
    public void run(){
        while (true){
            l.lock();
            if(ticket > 0){
                try{
                    Thread.sleep(10);
                    System.out.println("线程" + Thread.currentThread().getName() + "--->第" + ticket);
                    ticket--;
                }catch (Exception e){
                    e.printStackTrace();
                }finally {
                    l.unlock();
                }
            }
        }
    }


//    public static synchronized void payTicket(){
//        while(true){
//
//            if(ticket > 0){
//                try{
//                    Thread.sleep(10);
//                }catch (Exception e){
//                    e.printStackTrace();
//                }
//                System.out.println("线程" + Thread.currentThread().getName() + "--->第" + ticket);
//                ticket--;
//            }
//        }
//
//    }
}
