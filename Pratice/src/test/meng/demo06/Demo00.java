package test.meng.demo06;
import java.util.ArrayList;
import java.util.Arrays;

public class Demo00 {
    public static void main(String[] args) {
        String str = "akasfafoiwen7sd83";
        char[] str1 = str.toCharArray();
        sortArray(str1);
    }
    public static void sortArray(char[] a){
        Arrays.sort(a);
        for(int i = a.length - 1; i >= 0; i--){
            System.out.print(a[i]);
        }

    }
}
