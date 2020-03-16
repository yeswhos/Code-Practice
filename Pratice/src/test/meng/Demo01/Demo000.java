package test.meng.Demo01;

public class Demo000 {
    public static void main(String[] args) {
        System.out.println(sum(1,2));
        System.out.println(sum((long)65536,65536));
        int [] a = null;
        a = new int [4];
        System.out.println(a[3]);
    }
    public static boolean sum(int a, int b){
        if(a == b){
            return true;
        }
        else
            return false;
    }
    public static boolean sum(byte a, byte b){
        if(a == b){
            return true;
        }
        else
            return false;
    }
    public static boolean sum(short a, short b){
        if(a == b){
            return true;
        }
        else
            return false;
    }
    public static boolean sum(long a, long b){
        if(a == b){
            return true;
        }
        else
            return false;
    }
}
