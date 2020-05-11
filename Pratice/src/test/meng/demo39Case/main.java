package test.meng.demo39Case;

public class main {
    public static void main(String[] args) {
        Baozi baozi = new Baozi();
        new BaoZiPu(baozi).start();
        new ChiHuo(baozi).start();
    }
}
