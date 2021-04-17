class Tana{
    private String grilName;

    public Tana(){}

    public  Tana(String name){
        grilName = name;
    }


    public void setGrilName(String name){
        grilName = name;
    }

    public String getGrilName() {
        return grilName;
    }

    public void saying(){
        System.out.printf("你第一个女友的名字Your first gf Name:%s",getGrilName());
    }

}
