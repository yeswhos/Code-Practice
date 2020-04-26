package test.meng.demo30HashCode;

import java.util.Objects;

public class Demo04Student {
    private int age;
    private String name;

    public Demo04Student(){

    }
    public Demo04Student(int age, String name){
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "age is: " + age + " name is: "  + name + "||";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Demo04Student that = (Demo04Student) o;
        return /*age == that.age && */
                Objects.equals(name, that.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(/*age,*/ name);
    }

    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }

    public void setAge(int age){
        this.age = age;
    }

    public void setName(String name) {
        this.name = name;
    }
}
