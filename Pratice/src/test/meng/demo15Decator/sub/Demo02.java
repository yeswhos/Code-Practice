package test.meng.demo15Decator.sub;

import test.meng.demo15Decator.Demo00;

public class Demo02 extends Demo00 {
    public void Demo02(){
        Demo00 demo00 = new Demo00();
        System.out.println(demo00.num + super.num1 /*+ demo00.num2 + demo00.num3 */);
    }
}
