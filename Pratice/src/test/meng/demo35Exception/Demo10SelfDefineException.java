package test.meng.demo35Exception;

public class Demo10SelfDefineException extends Exception{
    public Demo10SelfDefineException(){
        super();
    }
    public Demo10SelfDefineException(String message){
        super(message);
    }
}
