package test.meng.demo26DeDeDeDeDeDe;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class Demo00Main {
    public static void main(String[] args) {
        ArrayList<String> poke = new ArrayList<>();
        String [] color = {"♠", "♥", "♣", "♦"};
        String [] numbers = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};
        for(String i: color){
            for(String j: numbers){
                poke.add(i + j);
            }

        }
        poke.add("大王");
        poke.add("小王");
        //System.out.println(poke);

        Collections.shuffle(poke);

        ArrayList<String> player0 = new ArrayList<>();
        ArrayList<String> player1 = new ArrayList<>();
        ArrayList<String> player2 = new ArrayList<>();
        ArrayList<String> dipai = new ArrayList<>();
        for(int i = 0; i < poke.size(); i++){
            String p = poke.get(i);
            if(i < 51){
                if(i % 3 == 0){
                    player0.add(p);
                }
                if(i % 3 == 1){
                    player1.add(p);
                }
                if(i % 3 == 2){
                    player2.add(p);
                }
            }
            else{
                dipai.add(p);
            }
        }
        System.out.println(player0);
        System.out.println(player1);
        System.out.println(player2);
        System.out.println(dipai);
    }
}
