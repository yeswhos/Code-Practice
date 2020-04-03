package test.meng.demo08Extend;

import java.util.ArrayList;
import java.util.Random;

public class Member extends User {
    public Member(){

    }
    public Member(int money, String name){
        super(name, money);
    }
    public void receive(ArrayList<Integer> pack){
        int index = new Random().nextInt(pack.size());
        int delete = pack.remove(index);
        int money = super.getMoney();
        super.setMoney(delete + money);
    }
}
