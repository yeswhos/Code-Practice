package test.meng.demo39Case;

public class ChiHuo extends Thread{
    private Baozi baozi;

    public ChiHuo(Baozi baozi) {
        this.baozi = baozi;
    }

    @Override
    public void run() {
        while (true){
            synchronized (baozi){
                if(baozi.flag == false){
                    try{
                        baozi.wait();
                    }catch (InterruptedException e){
                        e.printStackTrace();
                    }
                }
                System.out.println("正在吃" + baozi.pi + baozi.xian + "的包子");
                baozi.flag = false;
                baozi.notify();
                System.out.println("吃完了，去生产");
                System.out.println("----------------------------");
            }
        }
    }
}
