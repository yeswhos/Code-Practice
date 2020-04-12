package test.meng.demo18MemVarInterface;

public class Demo00Hero {
    private String name;
    private Demo01Skill demo01Skill;
    public Demo00Hero(){

    }
    public Demo00Hero(String name, Demo01Skill demo01Skill){
        this.name = name;
        this.demo01Skill = demo01Skill;
    }
    public void Attack(){
        //System.out.println(demo01Skill);
        demo01Skill.use();
    }
    public String getName(){
        return this.name;
    }
    public void setName(String name){
        this.name = name;
    }
    public Demo01Skill getDemo01Skill(){
        return this.demo01Skill;
    }
    public void setDemo01Skill(Demo01Skill demo01Skill){
        this.demo01Skill = demo01Skill;
    }
}
