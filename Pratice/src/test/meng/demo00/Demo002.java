package test.meng.demo00;

public class Demo002 {
    public static int sum(){
        int i;
        int j = 0;
        for(i = 1; i <= 100; i++){
            j = j + i;
        }
        return j;
    }
    public static void main(String[] args){
        System.out.println(sum());
    }
}
