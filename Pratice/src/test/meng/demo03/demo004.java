package test.meng.demo03;
import java.util.*;
public class demo004 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int f = 0;
        int [] d = new int[] {a, b, c};
        for(int i = 0; i < d.length; i++){
            if(d[i] > f){
                f = d[i];
            }
        }
        System.out.println(f);
    }
}
