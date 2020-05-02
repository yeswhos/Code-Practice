package test.meng.demo35Exception;

public class Demo02 {
    public static int getElement(int [] arr, int index){
        if(arr == null){
            throw new NullPointerException("空");
        }
        if(index > arr.length || index < 0){
            throw new ArrayIndexOutOfBoundsException("太长");
        }
        int ele = arr[index];
        return ele;
    }

    public static void main(String[] args) {
//        int[] arr = null;
//        getElement(arr, 0);
        int[] arr1 = {1, 2};
        getElement(arr1, 3);
    }

}
