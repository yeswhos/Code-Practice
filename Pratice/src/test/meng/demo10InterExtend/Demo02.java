package test.meng.demo10InterExtend;

public interface Demo02 extends Demo00, Demo01 {
    public abstract void method02();

    @Override
    public default void method0(){
        System.out.println("重写");
    }
}
