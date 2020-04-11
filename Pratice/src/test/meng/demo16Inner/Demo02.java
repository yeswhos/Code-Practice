package test.meng.demo16Inner;

public class Demo02 {
    public int num = 10;
    public class Inner{
        int num = 20;
        public void Method(){
            int num = 30;
            System.out.println(num);
            System.out.println(this.num);
            System.out.println(Demo02.this.num);
        }
    }
}
