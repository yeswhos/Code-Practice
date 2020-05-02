package test.meng.demo35Exception;

import java.util.Objects;

public class Demo03 {
    public static void main(String[] args) {
        //method(null);
        alterMethod(null);
    }
    public static void method(Object obj){
        Objects.requireNonNull(obj,"kong");
    }
    public static void alterMethod(Object obj){
        if(obj == null){
            throw new NullPointerException("kongkong");
        }
    }
}
