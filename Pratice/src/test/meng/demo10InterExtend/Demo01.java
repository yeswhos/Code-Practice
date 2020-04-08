package test.meng.demo10InterExtend;

public interface Demo01 {
    public abstract void method01();
    public abstract void method();
    public default void method0(){
        System.out.println("默认方法B");
    }
}
