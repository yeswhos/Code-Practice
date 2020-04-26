package test.meng.demo32CollectionMethod;

public class Demo02Person implements Comparable<Demo02Person>{
    private int age;
    private String name;

    public Demo02Person(int age, String name) {
        this.age = age;
        this.name = name;
    }

    @Override
    public String toString() {
        return "name is: " + this.name + ", age is: " + age;
    }

    @Override
    public int compareTo(Demo02Person o) {
        return this.getAge() - o.getAge();
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }
    
}
