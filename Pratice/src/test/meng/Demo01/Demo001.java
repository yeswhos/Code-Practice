package test.meng.Demo01;

public class Demo001 {
    public static void main(String[] args) {
        int [] a = new int []{1, 2, 3, 4, 5};
        for(int i = 0, j = a.length - 1; i < j; i++, j--){
            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
        for(int i = 0; i < a.length; i++){
            System.out.print(a[i]);
        }

    }
}
