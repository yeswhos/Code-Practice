package test.meng.demo40ThreadAndLambda;

public class Demo04Lambda01{
    public static void main(String[] args) {
        invokeCook(new Cook() {
            @Override
            public void makeFood() {
                System.out.println("匿名内部类");
            }
        });

        invokeCook(()->{
            System.out.println("lambda");
        });
        System.out.println("------------------");
        invokeCook(()-> System.out.println("lambda"));
    }

    public static void invokeCook(Cook cook) {
        cook.makeFood();
    }
}
