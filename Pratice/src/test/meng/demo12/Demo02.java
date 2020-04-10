package test.meng.demo12;

public class Demo02 {
    public static void main(String[] args) {
        Demo00 demo00 = new Demo01();
        demo00.method00();
        Demo01 demo01 = (Demo01) demo00;
        demo01.method01();
    }
}
