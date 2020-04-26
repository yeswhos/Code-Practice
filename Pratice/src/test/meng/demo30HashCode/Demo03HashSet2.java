package test.meng.demo30HashCode;

import java.util.HashSet;

public class Demo03HashSet2 {
    public static void main(String[] args) {
        Demo04Student stu1 = new Demo04Student(18, "Fanhui");
        Demo04Student stu2 = new Demo04Student(23, "Fanhui");

        System.out.println(stu1);
        System.out.println(stu2);

        System.out.println("hash code: " + stu1.hashCode());
        System.out.println("hash code: " + stu2.hashCode());
        HashSet<Demo04Student> set = new HashSet<>();
        set.add(stu1);
        set.add(stu2);
        System.out.println("set: " + set);
    }
}
