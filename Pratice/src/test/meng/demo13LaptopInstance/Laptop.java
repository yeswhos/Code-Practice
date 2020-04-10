package test.meng.demo13LaptopInstance;

public class Laptop {
    public static void powerOff(){
        System.out.println("power off");
    }
    public static void powerOn(){
        System.out.println("power on");
    }
    public static void useDevice(USB usb){
        if (usb instanceof KeyBoard){
            KeyBoard keyBoard = (KeyBoard) usb;
            usb.openDevice();
            keyBoard.type();
            usb.closeDevice();
        }
        else if(usb instanceof Mouse){
            Mouse mouse = (Mouse) usb;
            usb.openDevice();
            mouse.click();
            usb.closeDevice();
        }
    }

}
