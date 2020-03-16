package test.meng.demo05;

public class Student {
    private String name;
    private int age;
    private int id;
    private int counter = 0;
    static String add;
    public Student(){
        this.id = ++counter;
    }
    public Student(String name, int age){
        this.name = name;
        this.age = age;
        this.id = ++counter;
    }

    public int getAge() {
        return age;
    }

    public int getId() {
        return id;
    }
    public String getName(){
        return name;
    }
    public String getAdd(){
        return add;
    }
    public void setName(String name){
        this.name = name;
    }
    public void setAge(int age){
        this.age = age;
    }
    public void setId(int id){
        this.id = id;
    }
    public void setAdd(String add){
        this.add = add;
    }
}
