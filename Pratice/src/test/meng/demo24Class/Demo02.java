package test.meng.demo24Class;

public class Demo02 {
    public static void main(String[] args) {
        int a = 100;
        String s1 = a + "abc";
        System.out.println(s1);

        String s2 = Integer.toString(200);
        System.out.println(s2);

        String s3 = String.valueOf(300);
        System.out.println(s3);

        int b = Integer.parseInt("123");
        System.out.println(b);

        double c = Double.parseDouble("2.2222");
        System.out.println(c);

    }
}
