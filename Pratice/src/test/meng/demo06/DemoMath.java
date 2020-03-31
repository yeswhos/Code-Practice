package test.meng.demo06;

public class DemoMath {
    public static void main(String[] args) {
        double min = -10.8;
        double max = 5.9;
        int num;
        int counter = 0;
        for(num = (int)min; num <= Math.ceil(max); num++){
            counter++;
            int c = Math.abs(num);
            if((c <= 6) && (c >= 2.1)){
                counter--;
            }

        }
        System.out.println(counter);
    }
}
