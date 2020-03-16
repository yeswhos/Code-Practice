package test.meng.demo03;
import java.util.*;

public class demo005 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random r = new Random();

        int num = r.nextInt(100);
        while(true){
            int input = sc.nextInt();
            if(input > num){
                System.out.println("too large");
            }
            else if(input < num){
                System.out.print("too small");
            }
            else{
                System.out.println(num + "you're right");
                break;
            }

        }


    }
}
