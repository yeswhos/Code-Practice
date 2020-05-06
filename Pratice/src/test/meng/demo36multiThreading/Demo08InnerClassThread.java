package test.meng.demo36multiThreading;

public class Demo08InnerClassThread {
    public static void main(String[] args) {
        new Thread(){
            @Override
            public void run() {
                for(int i =0; i < 5; i++){
                    System.out.println("第一次" + i);
                }

            }
        }.start();

        Runnable a = new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i < 5; i++){
                    System.out.println("第二次" + i);
                }

            }
        };
        new Thread(a).start();
    }
}
