package test.meng.demo25Collection.genericMethod;

public class Demo06Method {
    public <E> void Demo00(E e){
        System.out.println(e);
    }
    public static <E> void Demo01(E e){
        System.out.println("static method:" + e);
    }
}
