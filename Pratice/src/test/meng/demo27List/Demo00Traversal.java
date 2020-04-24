package test.meng.demo27List;

import java.util.Iterator;
import java.util.List;

public class Demo00Traversal {
    public void traversal00(List<String> list){
        for(int i = 0; i < list.size(); i++){
            System.out.println("第一种" + list.get(i));
        }
    }

    public void traversal01(List<String> list){
        Iterator<String> it = list.iterator();
        while(it.hasNext()){
            System.out.println("第二种：" + it.next());
        }
    }

    public void traversal02(List<String> list){
        for(String s: list){
            System.out.println("第三种: " + s);
        }
    }
}
