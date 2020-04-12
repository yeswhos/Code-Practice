package test.meng.demoSummary;

import test.meng.demoSummary.red.RedPacketFrame;

public class Demo00 {
    public static void main(String[] args) {
        Demo01 demo01 = new Demo01("Red Packet");
        demo01.setOwnerName("Fanhui");

//        Demo02 demo02 = new Demo02();
//        demo01.setOpenWay(demo02);

        Demo03 demo03 = new Demo03();
        demo01.setOpenWay(demo03);
    }
}
