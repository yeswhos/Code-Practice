package test.meng.demo40ThreadAndLambda;

public class Demo03Lambda {
    public static void main(String[] args) {
        new Thread(()->{
            System.out.println(Thread.currentThread().getName() + "线程运行");
        }).start();
        System.out.println("-----------------------");
        new Thread(()-> System.out.println(Thread.currentThread().getName() + "线程运行")).start();
    }
}
