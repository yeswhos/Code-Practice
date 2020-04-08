package test.meng.demo10InterExtend;

public interface Demo00 {
    public abstract void method00();
    public abstract void method();
    public default void method0(){
        System.out.println("默认方法A");
    }
}
