package test.meng.demo11Polymorphism;

public class Demo02 {
    public static void main(String[] args) {
        Demo00 demo01 = new Demo01();
        System.out.println(demo01.num);
        //((Demo01) demo01).show();
        demo01.show();
        demo01.method();
        demo01.method00();

    }
}
