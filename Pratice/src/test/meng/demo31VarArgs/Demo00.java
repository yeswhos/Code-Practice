package test.meng.demo31VarArgs;

public class Demo00 {
    public static void main(String[] args) {
        int result = add(1, 2, 3, 4);
        System.out.println(result);
    }
    public static int add(int... arr){
        int sum = 0;
        for(int i: arr){
            sum += i;
        }
        return sum;
    }
}
