package test.meng.demoSummary;

import test.meng.demoSummary.red.OpenMode;

import java.util.ArrayList;
import java.util.Random;

public class Demo03 implements OpenMode {
    @Override
    public ArrayList<Integer> divide(int totalMoney, int totalCount) {
        Random r = new Random();
        ArrayList list = new ArrayList();
        int LeftMoney = totalMoney;
        int LeftCount = totalCount;
        for(int i = 0; i < totalCount - 1; i++){
            int money = r.nextInt(LeftMoney / LeftCount * 2) + 1;
            LeftMoney = LeftMoney - money;
            LeftCount--;
            list.add(money);
        }
        list.add(LeftMoney);
        return list;
    }
}
