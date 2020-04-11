package test.meng.demo16Inner;

public class Demo01Main {
    public static void main(String[] args) {
        Demo00 demo00 = new Demo00();
        demo00.Use();
        System.out.println("======================");
        Demo00.Demo00Inner inner = new Demo00().new Demo00Inner();
        inner.Inner();
        System.out.println("======================");
        Demo02.Inner inner1 = new Demo02().new Inner();
        inner1.Method();
    }
}
