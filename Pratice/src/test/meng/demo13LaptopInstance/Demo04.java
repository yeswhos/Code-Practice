package test.meng.demo13LaptopInstance;

public class Demo04 {
    public static void main(String[] args) {
        Laptop laptop = new Laptop();
        laptop.powerOn();
        //USB usb = new KeyBoard();
        USB usb = new Mouse();
        laptop.useDevice(new KeyBoard());
        laptop.useDevice(usb);
        laptop.powerOff();
    }
}
