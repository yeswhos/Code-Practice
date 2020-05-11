package test.meng.demo39Case;

public class BaoZiPu extends Thread{
    private Baozi baozi;
    public BaoZiPu(Baozi baozi){
        this.baozi = baozi;
    }

    @Override
    public void run() {
        int count = 0;
        synchronized (baozi){
            while (true){
                if(baozi.flag == true){
                    try{
                        baozi.wait();
                    }catch (Exception e){
                        e.printStackTrace();
                    }
                }
                if(count % 2 == 0){
                    baozi.pi = "pi 1";
                    baozi.xian = "xian 1";
                    count++;
                }
                else{
                    baozi.pi = "pi 2";
                    baozi.xian = "xian 2";
                    count++;
                }
                try{
                    Thread.sleep(2000);
                }catch (InterruptedException e){
                    e.printStackTrace();
                }
                baozi.flag = true;
                baozi.notify();
                System.out.println("生产好了" + baozi.pi + baozi.xian + "好了");
            }
        }
    }
}
