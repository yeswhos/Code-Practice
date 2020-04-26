package test.meng.demo30HashCode;

public class Demo00Main {
    public static void main(String[] args) {
        Demo01Person p1 = new Demo01Person();
        int i1 = p1.hashCode();
        System.out.println(i1);
        Demo01Person p2 = new Demo01Person();
        int i2 = p2.hashCode();
        System.out.println(i2);

        String s1 = new String("ABC");
        int s2 = s1.hashCode();
        System.out.println(s2);
    }
}
