package test.meng.demo18MemVarInterface;

public class Demo02Main {
    public static void main(String[] args) {
        Demo00Hero demo00Hero = new Demo00Hero();
        demo00Hero.setName("德莱文");
        demo00Hero.setDemo01Skill(new Demo01Skill(){
            @Override
            public void use(){
                System.out.println("斧子");
            }
        });
        System.out.println(demo00Hero.getName());
        demo00Hero.Attack();
        Demo01Skill obj = new Demo01Skill() {
            @Override
            public void use() {
                System.out.println("斧子A");
            }
        };
        obj.use();
        demo00Hero.setDemo01Skill(obj);
    }
}
