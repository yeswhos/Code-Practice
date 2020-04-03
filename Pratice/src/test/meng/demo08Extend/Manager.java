package test.meng.demo08Extend;

import java.util.ArrayList;

public class Manager extends User {
    public Manager(){

    }
    public Manager(int money, String name){
//        money = super.money;
//        name = super.name;
        super(name, money);
    }
    public ArrayList<Integer> send(int totalMoney, int count){
        ArrayList<Integer> pack = new ArrayList<Integer>();
        int leftMoney = super.getMoney();
        if(totalMoney > leftMoney){
            System.out.println("余额不足");
            return pack;
        }
        setMoney(leftMoney - totalMoney);
        int ave = totalMoney / count;
        int last = totalMoney % count;
        for(int i =  0; i < count; i++){
            pack.add(ave);
        }
        pack.add(ave + last);
        return pack;
    }
}
