package test.meng.demo35Exception;

import java.util.Scanner;

/*
    模拟注册操作，如果用户名已经存在，抛出异常并提示
 */
public class Demo11Case extends Exception{
    public Demo11Case(){
        super();
    }
    public Demo11Case(String str){
        super(str);
    }
    static String[] usernames = {"Fanhui", "Lulu"};
    public static void main(String[] args) /*throws Demo11Case */{
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入用户名");
        String username = sc.next();
        check(username);
    }
    public static void check(String username) /* throws Demo11Case */{
        for(String name : usernames){
//            if(name.equals(username)){
//                throw new Demo11Case("已经被注册");
//            }
            if(name.equals(username)){
                try{
                    throw new Demo11Case("已被注册");
                }catch (Demo11Case e){
                    e.printStackTrace();
                    return;
                }
            }
        }
        System.out.println("Success");
    }
}
