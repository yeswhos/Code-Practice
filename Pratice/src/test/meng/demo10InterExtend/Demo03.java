package test.meng.demo10InterExtend;

public class Demo03 implements Demo02 {

    @Override
    public void method02() {
        System.out.println("Override Demo02");
    }
    @Override
    public void method(){
        System.out.println("override method()");
    }
    @Override
    public void method00(){
        System.out.println("override method00()");
    }
    @Override
    public void method01(){
        System.out.println("override method01()");
    }

}
