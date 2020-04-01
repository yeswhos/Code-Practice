package test.meng.demo07;

public class Demo02Son extends Demo01Father{
    int a = 10;
    public void test(){
        int a = 20;
        System.out.println(a);
        System.out.println(this.a);
        System.out.println(super.a);
    }
//    public void method(){
//        System.out.println("Son");
//    }

}
