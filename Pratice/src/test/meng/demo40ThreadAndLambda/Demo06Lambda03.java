package test.meng.demo40ThreadAndLambda;

public class Demo06Lambda03 {
    public static int invokeCalc(Calculator cal, int a, int b){
        return cal.sum(a, b);
    }

    public static void main(String[] args) {
        System.out.println(invokeCalc(new Calculator() {
            @Override
            public int sum(int a, int b) {
                return a + b;
            }
        }, 120, 130));
        System.out.println("-----------------------");
        System.out.println(invokeCalc((int a, int b)->{
            return a + b;
        }, 120, 130));
    }
}
