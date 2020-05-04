package test.meng.demo35Exception;

public class Demo09SuperClass {
    public void show01() throws NullPointerException, ClassCastException{}
    public void show02() throws IndexOutOfBoundsException{}
    public void show03() throws IndexOutOfBoundsException{};
    public void show04() throws Exception{}
}

class subClass extends Demo09SuperClass{
    public void show01() throws NullPointerException, ClassCastException{}
    public void show02() throws ArrayIndexOutOfBoundsException{}
    public void show03(){}
    public void show04(){
        try{
            throw new Exception("编译期异常");
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
