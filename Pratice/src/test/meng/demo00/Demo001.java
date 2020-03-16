package test.meng.demo00;

public class Demo001 {
    public static void main(String[] args){
        int a = 5;
        int b = 8;
        System.out.println(compare(a,b));
    }
    public static boolean compare(int a, int b){
/*        boolean c;
        if(a > b){
            c = true;
        }
        else{
            c = false;
        }
        return c;*/
        return a == b;
    }
}
