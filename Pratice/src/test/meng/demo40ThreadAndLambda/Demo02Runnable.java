package test.meng.demo40ThreadAndLambda;

public class Demo02Runnable {
    public static void main(String[] args) {
        Demo01RunImp run = new Demo01RunImp();
        Thread t = new Thread(run);
        t.start();
        System.out.println("开启线程" + Thread.currentThread().getName());
        System.out.println("------------------------");

        Runnable r = new Runnable() {
            @Override
            public void run() {
                System.out.println("开启线程" + Thread.currentThread().getName());
            }
        };
        new Thread(r).start();
        System.out.println("------------------------");

        new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("开启线程" + Thread.currentThread().getName());
            }
        }).start();
    }
}
