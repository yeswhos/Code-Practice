package test.meng.demo09Interface;

public interface Demo00 {
    public abstract void AB();
    public default void ABC(){
        System.out.println("ABC");
    }
}
