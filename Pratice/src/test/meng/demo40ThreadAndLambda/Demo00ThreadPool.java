package test.meng.demo40ThreadAndLambda;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Demo00ThreadPool {
    public static void main(String[] args) {
        ExecutorService es = Executors.newFixedThreadPool(2);
        es.submit(new Demo01RunImp());
        es.submit(new Demo01RunImp());
        es.submit(new Demo01RunImp());
//        es.shutdown();
    }
}
