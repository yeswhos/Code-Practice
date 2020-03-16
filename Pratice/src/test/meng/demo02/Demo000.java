package test.meng.demo02;

public class Demo000 {
    public String name;
    private int age;
    public void setAge(int num){
        age = num;
    }
    public int getAge(){
       return age;
    }
    public void show(){
        System.out.println(name + age);
    }
}
