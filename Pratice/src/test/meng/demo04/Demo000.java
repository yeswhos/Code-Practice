package test.meng.demo04;

public class Demo000{
    public static void main(String[] args) {
        int [] a = {1, 2, 3};

        System.out.println(combineString(a));


    }

    private static String combineString(int [] source) {
        String result = "[";

        for(int i = 0 ; i < source.length; i ++) {

            result += source[i];
            if(i != source.length - 1)
                result += "#";

        }
        result += "]";
        return result;
    }
}