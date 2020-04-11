package test.meng.demo16Inner;

public class Demo00 {
    public class Demo00Inner{
        public void Inner(){
            System.out.println("Inner Method");
            Own();
        }

    }
    public void Use(){
        Demo00Inner demo00Inner = new Demo00Inner();
        demo00Inner.Inner();
        //anonymity
        new Demo00Inner().Inner();
    }
    public void Own(){
        System.out.println("outsider");
    }
}
