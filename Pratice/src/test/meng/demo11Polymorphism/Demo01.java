package test.meng.demo11Polymorphism;

public class Demo01 extends Demo00 {
    int num = 20;
    @Override
    public void show(){
        System.out.println(num);
    }
    @Override
    public void method(){
        System.out.println("methodSon");
    }
}
