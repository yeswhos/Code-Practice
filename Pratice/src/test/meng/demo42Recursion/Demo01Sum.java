package test.meng.demo42Recursion;

public class Demo01Sum {
    public static int Sum(int i){
        if(i == 1){
            return 1;
        }
//        i += Sum(i - 1);
        return i + Sum(i - 1);
    }

    public static void main(String[] args) {
        int a = 0;
        a = Sum(10);
        System.out.println(a);
    }
}
