package test.meng.demo38ThreadStatus;

public class Demo01WaitSleep {
    public static void main(String[] args) {
        Object obj = new Object();
        new Thread(){
            @Override
            public void run() {
                while (true){
                    synchronized (obj){
                        System.out.println("顾客1：买咸鸭蛋");
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
                while (true){
                    synchronized (obj){
                        System.out.println("顾客2：买咸鸭蛋");
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
                    try {
                        Thread.sleep(5000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    synchronized (obj){
                        System.out.println("5毛钱俩，一块钱不卖");

//                        obj.notify();
                        obj.notifyAll();
                        System.out.println("给你");
                    }

                }
            }
        }.start();
    }
}
