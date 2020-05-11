package test.meng.demo37threadSecurity;

import test.meng.demo36multiThreading.Demo09Security;

public class Demo01Main {
    public static void main(String[] args) {
//        Demo00Synchronized run = new Demo00Synchronized();
//        Demo02SynMethod run = new Demo02SynMethod();
        Demo03Lock run = new Demo03Lock();
        Thread t0 = new Thread(run);
        Thread t1 = new Thread(run);
        Thread t2 = new Thread(run);
        t0.start();
        t1.start();
        t2.start();
    }

}
