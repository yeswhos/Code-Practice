package test.meng.demo23StringBuilder;

public class Demo00 {
    public static void main(String[] args) {
        /*
        构造
         */
        StringBuilder str1 = new StringBuilder();
        StringBuilder str2 = new StringBuilder("abc");
        /*
        方法
         */
        str1.append("a").append("b").append("c");
        str2.toString();
        System.out.println(str1);
        System.out.println(str2);
    }
}
