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

    //重写equal
    @Override
    public boolean equals(Object obj){
        //提高程序效率
        if(obj == null){
            return false;
        }
        if(obj == this){
            return true;
        }

        //增加判断，防止classcastexpection
        if (obj instanceof Demo00){
            //强制转换
            Demo00 demo00 = (Demo00) obj;
            boolean b = this.name == demo00.name && this.age == demo00.age;
            return b;
        }
        return false;
    }
}
