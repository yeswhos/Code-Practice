package test.meng.demo25Collection.generic;

public class Demo05GenericMain {
    public static void main(String[] args) {
        Demo04GenericClass<Integer> g1 = new Demo04GenericClass<>();
        g1.setName(1);
        int a = g1.getName();
        System.out.println(a);

        Demo04GenericClass<String> g2 = new Demo04GenericClass<>();
        g2.setName("Fanhui");
        String b = g2.getName();
        System.out.println(b);

    }
}
