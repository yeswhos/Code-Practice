package test.meng.demo34DeDeDeDeUpgrade;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class Demo00Main {
    public static void main(String[] args) {
        HashMap<Integer, String> poker = new HashMap<>();
        ArrayList<Integer> pokerIndex = new ArrayList<>();

        List<String> color = List.of("♠", "♥", "♣", "♦");
        List<String> numbers = List.of("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K");

        int index = 0;
        poker.put(index, "大王");
        pokerIndex.add(index);
        index++;
        poker.put(index, "小王");
        pokerIndex.add(index);
        index++;
        for(String str : numbers){
            for(String col : color){
                poker.put(index, col + str);
                pokerIndex.add(index);
                index++;
            }
        }
        System.out.println(poker);

        //shuffle
        Collections.shuffle(pokerIndex);

        //发牌
        ArrayList<Integer> player00 = new ArrayList<>();
        ArrayList<Integer> player01 = new ArrayList<>();
        ArrayList<Integer> player10 = new ArrayList<>();
        ArrayList<Integer> player11 = new ArrayList<>();

        for(int i = 0; i < pokerIndex.size(); i++){
            Integer in = pokerIndex.get(i);
            if(i < 51){
                if(i % 3 == 0){
                    player00.add(in);
                }
                else if(i % 3 == 1){
                    player01.add(in);
                }
                else if(i % 3 == 2){
                    player10.add(in);
                }
            }
            else{
                player11.add(in);
            }
        }
        Collections.sort(player00);
        Collections.sort(player01);
        Collections.sort(player10);
        Collections.sort(player11);
        //看牌
        show("55开", poker, player00);
        show("大司马", poker, player01);
        show("PDD", poker, player10);
        show("底牌", poker, player11);
    }
    public static void show(String name, HashMap<Integer, String> map, ArrayList<Integer> list){
        System.out.println("name is: " + name);
        for(Integer i : list){
            String value = map.get(i);
            System.out.print(value + " ");
        }
    }
}
