public class Player
{
    private String name;
    private int roll;
    private int hp;
    private int hpCap;
    private int number;

    public String getName()
    {
      return name;
    }
    public void setName(String name)
    {
      this.name = name;
    }

    public int getRoll()
    {
      return roll;
    } 
    public void setRoll(int roll)
    {
      this.roll = roll;
    }

    public void setHp(int hp)
    {
      if(hp>hpCap)
      {
        setHpCap(hp);
      }
      this.hp = hp;
    }
    public int getHp()
    {
      return hp;
    }

    private void setHpCap(int hp)
    {
      hpCap = hp;
    }
    
    public void setNumber(int num)
    {
      number = num;
    }
    public int getNumber()
    {
      return number;
    }

    public void heal(int newHp)
    {
      if(hp+newHp>hpCap)
      {
        hp = hpCap;
      }
      else
        hp+=newHp;
    }
    public void damage(int newhp)
    {
      if(this.hp-newhp<0)
      {
        this.hp = 0;
      }
      else
        this.hp-=newhp;
    }
}