package test.meng.demo17Anonymous;

public class Demo01Main {
    public static void main(String[] args) {
        Demo00 obj = new Demo00() {
            @Override
            public void Method() {
                System.out.println("Method1");
            }

            @Override
            public void MethodAlter() {
                System.out.println("Method2");
            }
        };
        obj.Method();
        obj.MethodAlter();

        new Demo00() {
            @Override
            public void Method() {
                System.out.println("Method1");
            }

            @Override
            public void MethodAlter() {
                System.out.println("Method2");
            }
        }.Method();
    }
}
