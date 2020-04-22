package test.meng.demo25Collection.generic;

public class Demo04GenericClass <E>{
    private E name;
    public Demo04GenericClass(){
    }
    public void setName(E name){
        this.name = name;
    }
    public E getName(){
        return this.name;
    }
}
