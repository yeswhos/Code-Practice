package test.meng.demo40ThreadAndLambda;

public class Demo01RunImp implements Runnable{
    @Override
    public void run() {
        System.out.println("创建新线程" + Thread.currentThread().getName());
    }
}
