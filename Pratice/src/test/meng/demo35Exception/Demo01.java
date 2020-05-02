package test.meng.demo35Exception;

public class Demo01 {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3};
        getElement(arr, 4);
    }
    public static int getElement(int [] arr, int index){
       int ele = arr[index];
       return ele;
    }
}
