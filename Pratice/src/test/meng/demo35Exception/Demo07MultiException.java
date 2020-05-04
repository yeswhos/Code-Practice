package test.meng.demo35Exception;

import java.util.List;

public class Demo07MultiException {
    public static void main(String[] args) {
        try{
            int[] arr = {1, 2, 3};
            System.out.println(arr[3]);
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println(e);
        }
        try {
            List<Integer> list = List.of(1, 2, 3);
            System.out.println(list.get(3));
        }catch (IndexOutOfBoundsException e){
            System.out.println(e);
        }
        System.out.println("-----------------------");
        /*
        如果catch里有子父类关系，子类必须写在父类上面，否则会报错
        ArrayIndexOutOfBoundsException extends IndexOutOfBoundsException
         */
        try{
            int[] arr = {1, 2, 3};
            System.out.println(arr[3]);
            List<Integer> list = List.of(1, 2, 3);
            System.out.println(list.get(3));
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println(e);
        }catch (IndexOutOfBoundsException e){
            System.out.println(e);
        }
        System.out.println("----------------");
        try{
            int[] arr = {1, 2, 3};
            System.out.println(arr[3]);
            List<Integer> list = List.of(1, 2, 3);
            System.out.println(list.get(3));
        } catch (Exception e){
            System.out.println(e);
        }
        System.out.println("--------------------");
        /*
        不处理，给虚拟机处理
         */
        int[] arr = {1, 2, 3};
        System.out.println(arr[3]);
        List<Integer> list = List.of(1, 2, 3);
        System.out.println(list.get(3));
    }
}
