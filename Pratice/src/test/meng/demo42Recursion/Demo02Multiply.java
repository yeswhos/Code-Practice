package test.meng.demo42Recursion;

public class Demo02Multiply {
    public static int times(int i){
        if(i == 1){
            return 1;
        }
        return i * times(i - 1);
    }

    public static void main(String[] args) {
        int a = 0;
        a = times(3);
        System.out.println(a);
    }
}
