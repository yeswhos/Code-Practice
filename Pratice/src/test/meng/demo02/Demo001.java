package test.meng.demo02;

public class Demo001 {
    public static void main(String[] args) {
        Demo000 demo000 = new Demo000();
        demo000.name = "Fanhui Meng";
        demo000.setAge(20);
        System.out.println(demo000.getAge());
        demo000.show();
    }
}
