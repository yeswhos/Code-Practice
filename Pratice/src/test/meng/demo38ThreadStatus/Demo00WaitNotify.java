package test.meng.demo38ThreadStatus;

public class Demo00WaitNotify {
    public static void main(String[] args) {
        Object obj = new Object();
        new Thread(){
            @Override
            public void run() {
                while (true){
                    synchronized (obj){
                        System.out.println("买咸鸭蛋");
                        try {
                            obj.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        System.out.println("买到了，");
                        System.out.println("----------------------------------");
                    }

                }
            }
        }.start();
        new Thread(){
            @Override
            public void run() {
                while(true){
                    synchronized (obj){
                        System.out.println("5毛钱俩，一块钱不卖");
                        try {
                            Thread.sleep(5000);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        obj.notify();
                        System.out.println("给你");
                    }

                }
            }
        }.start();
    }
}
