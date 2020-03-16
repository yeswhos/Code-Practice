package test.meng.demo00;

public class Demo003 {
    public static void printed(int a){
        for(int i = 0; i <= a; i++){
            System.out.println("pint" + i + "times");
        }
    }
    public static void main(String[] args){
        int a = 10;
        printed(a);
    }
}
