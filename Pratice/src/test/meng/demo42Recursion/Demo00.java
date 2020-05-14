package test.meng.demo42Recursion;

public class Demo00 {
    public static void show00(int i){
        System.out.println(i);
        i = i - 1;
        if(i == 0){
//            show00(i);
            return;
        }
        show00(i);

    }

    public static void main(String[] args) {
        int i = 10;
        show00(i);
    }
}
