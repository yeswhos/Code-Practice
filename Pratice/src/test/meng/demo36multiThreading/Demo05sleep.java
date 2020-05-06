package test.meng.demo36multiThreading;

public class Demo05sleep {
    public static void main(String[] args) {
        for(int i = 0; i < 10; i++){
            System.out.println(i);
            try{
                Thread.sleep(1000);
            }catch (InterruptedException e){
                e.printStackTrace();
            }

        }
    }
}
