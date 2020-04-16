package test.meng.demo19Summary;

import test.meng.demo19Summary.red.OpenMode;

import java.util.ArrayList;

public class Demo02 implements OpenMode {
    public ArrayList<Integer> divide(int totalMoney, int totalCount){
        ArrayList list = new ArrayList();
        int ave = totalMoney / totalCount;
        int rest = totalMoney % totalCount;
        for(int i = 0; i < totalCount - 1; i++){
            list.add(ave);
        }
        list.add(ave + rest);
        return list;
    }
}
