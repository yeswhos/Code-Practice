package test.meng.demo14Final;

public class Demo00 {
    //public final String name;
    public String name;
    public Demo00(){
        name = "Fanhui";
    }
    public Demo00(String name){
        this.name = name;
    }
    public final String getName(){
        return this.name;
    }
//    public void setName(String name){
//        this.name = name;
//    }
}
