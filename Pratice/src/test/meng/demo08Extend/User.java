package test.meng.demo08Extend;

public class User {
    public String name;
    public int money;

    public User(){

    }
    public User(String name, int money){
        this.name = name;
        this.money = money;
    }

    public void show(){
//        int money = getMoney();
//        String name = getName();
        System.out.println(money + "####" +  name);
    }
    public int getMoney(){
        return money;
    }
    public void setMoney(int money){
        this.money = money;
    }

    public String getName() {
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
}
