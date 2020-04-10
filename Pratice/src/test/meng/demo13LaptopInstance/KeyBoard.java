package test.meng.demo13LaptopInstance;

public class KeyBoard implements USB{
    @Override
    public void openDevice(){
        System.out.println("Open KeyBoard");
    }

    @Override
    public void closeDevice(){
        System.out.println("Close KeyBoard");
    }
    public void type(){
        System.out.println("type the keyboard");
    }
}
