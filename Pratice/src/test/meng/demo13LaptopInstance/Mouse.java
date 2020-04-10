package test.meng.demo13LaptopInstance;

public class Mouse implements USB{
    @Override
    public void openDevice(){
        System.out.println("Open Mouse");
    }

    @Override
    public void closeDevice(){
        System.out.println("Close Mouse");
    }

    public void click(){
        System.out.println("Click the mouse");
    }
}
