package test.meng.demo20Object;

public class Demo00 {
    private String name;
    private int age;
    public Demo00(){

    }
    public Demo00(String name, int age){
        this.name = name;
        this.age = age;
        toString();
    }

    @Override
    public String toString(){
        return "name:" + this.name + "Age:" + this.age;
    }

    public String getName() {
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
    public int getAge(){
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
