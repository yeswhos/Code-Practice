package test.meng.demo08Extend;

import java.util.ArrayList;

public class MainEntrance {
    public static void main(String[] args) {
        Manager manager = new Manager(100, "PDD");
        Member memberA = new Member(0, "大司马");
        Member memberB = new Member(0, "茄子");
        Member memberC = new Member(0, "团团");
        manager.show();
        ArrayList<Integer> pack = manager.send(50,3);
        memberA.receive(pack);
        memberB.receive(pack);
        memberC.receive(pack);
        manager.show();
        memberA.show();
        memberB.show();
        memberC.show();
    }

}
