import java.util.Scanner;

public class dnd
{

   static Scanner keyboard = new Scanner(System.in);

   public static void main(String[] args)
    {
      
      System.out.println("Only Wyatt can use this feature");
      System.out.println("So enter your super secret password:");
      String password = keyboard.nextLine();
      if(password.equals("xd"))
      {
        String[] commands = new String[10];
        commands[0] = "help, ";
        commands[1] = "setNames, ";
        commands[2] = "rollInit, ";
        commands[3] = "exit, ";
        commands[4] = "heal, ";
        commands[5] = "damage, ";
        commands[6] = "setHp, ";
        commands[7] = "listHps, ";
        commands[8] = "listNumbers";
        commands[9] = "roll";
        boolean itDo = true;

        System.out.print("How many people are playing? ");
        int number = keyboard.nextInt();
        Player[] players = new Player[number+1];
        for(int i = 0;i<players.length;i++)
        {
          players[i] = new Player();
          players[i].setNumber(i);
        }
        players = setNames(players);
        System.out.println("Names:");
        for(int i = 0;i<players.length;i++)
        {
          System.out.println(i+": "+players[i].getName());
        }
        System.out.println();
        System.out.println();
        for(int i = 1;i<players.length;i++)
        {
          System.out.print("What is "+players[i].getName()+"'s health cap? ");
          int hpCap = keyboard.nextInt();
          players[i].setHp(hpCap);
        }
        System.out.println("Hp's:");
        for(int i = 1;i<players.length;i++)
        {
          System.out.println(players[i].getName()+"'s hp is "+players[i].getHp());
        }
        System.out.println();
        System.out.println();
        keyboard.nextLine();

        while(itDo)
        {
          System.out.print("What would you like to do, 'O great one: ");
          String input = keyboard.nextLine();
          System.out.println();
          
          
          switch(input)
          {
            case "help":
              System.out.println("Type in a command from the following list and hit enter");
              System.out.println();
              System.out.print("Commands: ");  
              for(int i=0;i<commands.length;i++)
               {
                 System.out.print(commands[i]);
               }
               System.out.println();
               System.out.println();
           break;

            case "setNames": 
              System.out.print("How many people are playing? ");
              number = keyboard.nextInt();
              players = new Player[number+1];
              for(int i = 0;i<players.length;i++)
              {
                 players[i] = new Player();
                 players[i].setNumber(i);
              }
              players = setNames(players);
              System.out.println("Names:");
              for(int i = 0;i<players.length;i++)
              {
                System.out.println(i+": "+players[i].getName());
              }
              System.out.println();
              System.out.println();
              for(int i = 1;i<players.length;i++)
              {
                System.out.print("What is "+players[i].getName()+"'s health cap? ");
                int hpCap = keyboard.nextInt();
                players[i].setHp(hpCap);
              }
              System.out.println("Hp's:");
              for(int i = 1;i<players.length;i++)
              {
                System.out.println(players[i].getName()+"'s hp is "+players[i].getHp());
              }
              keyboard.nextLine();
              System.out.println();
              System.out.println();
            break;

            case "rollInit": 
              rollInit(players); 
            break;

            case "heal": 
              System.out.print("Which player would you like to heal? (name or number):");
              String player = keyboard.nextLine();
              System.out.print("How much would you like to heal them?");
              int hp = keyboard.nextInt();
              if(isInteger(player))
                healPlayer(Integer.parseInt(player),hp,players);
              else
                healPlayer(player,hp,players); 
            break;

            case "damage": 
              System.out.print("Which player would you like to damage? (name or number):");
              player = keyboard.nextLine();
              System.out.print("How much would you like to damage them by?");
              hp = keyboard.nextInt();
              if(isInteger(player))
                damagePlayer(Integer.parseInt(player),hp,players);
              else
                damagePlayer(player,hp,players);            
            break;

            case "setHp": 
              System.out.print("Which player would you like to set hp for? (name or number):");
              player = keyboard.nextLine();
              System.out.print("What would you like to set their hp to?");
              hp = keyboard.nextInt();
              if(isInteger(player))
                setPlayerHp(Integer.parseInt(player),hp,players);
              else
               setPlayerHp(player,hp,players);               
            break;

            case "listHps": 
              listHps(players);
            break;

            case "roll":
              System.out.print("What sided die would you like to roll? ");
              int sides = keyboard.nextInt();
              System.out.println("Your number is "+generateRandomNumber(sides));
              keyboard.nextLine();
              System.out.println();
            break;

            case "listNumbers": 
              listNumbers(players);
            break;

            case "exit":
              itDo = false; 
            break;

            default: System.out.println("Unkown, check spelling and try again");
          }
         }
      }
      else
      {
        System.out.println("Why are you gay. This is DM shit");
      }     
    }

   public static Player[] setNames(Player[] players)
   {
      keyboard.nextLine();
      for(int i = 1;i < players.length;i++)
      {
          System.out.print("Name of player "+i+": ");
          players[i].setName(keyboard.nextLine());
      }
      players[0].setName("Monsters");
      return players;
   }

  public static Player[] rollInit(Player[] players)
  {
     for(int i=0;i<players.length;i++)
     {
        players[i].setRoll((int)Math.ceil((Math.random()*20)));
     }
     for(int r = 0;r<players.length;r++)
     {
       for(int i = 1;i<players.length;i++)
       {
          if(players[i].getRoll()>players[i-1].getRoll())
          {
            Player temp = players[i];
            players[i] = players[i-1];
            players[i-1] = temp;
          }
       }
     }
     for(int i=0;i<players.length;i++)
     {
        System.out.println(players[i].getName()+"'s roll:"+players[i].getRoll());
     }
     System.out.println();

     return players;
  }

  public static void healPlayer(int number, int hp, Player[] players)
  {
      if(number>=1)
      {
        for(int i = 1;i<players.length;i++)
        {
          if(number == players[i].getNumber())
          {
              players[i].heal(hp);
              System.out.println(players[i].getName()+"'s new hp is "+players[i].getHp());
              System.out.println();
              keyboard.nextLine();
          }
       }
      }
      else
      {
        System.out.println("You gotta choose one of the players, bud... numbers start at 1");
      }
  }
  public static void healPlayer(String name, int hp, Player[] players)
  {
      for(int i = 0;i<players.length;i++)
      {
          if(name.equals(players[i].getName()))
          {
              players[i].heal(hp);
              System.out.println(players[i].getName()+"'s new hp is "+players[i].getHp());
              System.out.println();
              keyboard.nextLine();
          }
      }
  }

  public static void damagePlayer(int number, int hp, Player[] players)
  {
    if(number>=1)
    {
      for(int i = 1;i<players.length;i++)
      {
        if(number == players[i].getNumber())
        {
            players[i].damage(hp);
            System.out.println(players[i].getName()+"'s new hp is "+players[i].getHp());
            System.out.println();
            keyboard.nextLine();
        }
     }
    }
    else
    {
      System.out.println("You gotta choose one of the players, bud... numbers start at 1");
    }
  }
  public static void damagePlayer(String name, int hp, Player[] players)
  {
    for(int i = 0;i<players.length;i++)
    {
        if(name.equals(players[i].getName()))
        {
            players[i].damage(hp);
            System.out.println(players[i].getName()+"'s new hp is "+players[i].getHp());
            System.out.println();
            keyboard.nextLine();
        }
    }
  }

  public static void setPlayerHp(String name, int hp, Player[] players)
  {
    for(int i = 0;i<players.length;i++)
    {
        if(name.equals(players[i].getName()))
        {
            players[i].setHp(hp);
            System.out.println(players[i].getName()+"'s new hp is "+players[i].getHp());
            System.out.println();
            keyboard.nextLine();
        }
    }
  }
  public static void setPlayerHp(int number, int hp, Player[] players)
  {
    if(number>=1)
    {
      for(int i = 1;i<players.length;i++)
      {
        if(number == players[i].getNumber())
        {
            players[i].setHp(hp);
            System.out.println(players[i].getName()+"'s new hp is "+players[i].getHp());
            System.out.println();
            keyboard.nextLine();
        }
     }
    }
    else
    {
      System.out.println("You gotta choose one of the players, bud... numbers start at 1");
    }
  }

  public static void listHps(Player[] players)
  {
    for(int i = 1; i<players.length;i++)
    {
      System.out.println(players[i].getName()+"'s hp is "+players[i].getHp());
    }
    System.out.println();
  }
  public static void listNumbers(Player[] players)
  {
    for(int i = 1; i<players.length;i++)
    {
      for(int c = 0; c<players.length;c++)
      {
        if(players[c].getNumber() == i)
        {
          System.out.println(players[c].getName()+"'s number is "+players[c].getNumber());
        }
      }
    }
    System.out.println();

  }
  public static boolean isInteger(String s) 
  {
    return isInteger(s,10);
  }

  public static int generateRandomNumber(int sides)
  {
    return (int)Math.ceil(Math.random()*sides);
  }


  public static boolean isInteger(String s, int radix) 
  {
    if(s.isEmpty()) return false;
    for(int i = 0; i < s.length(); i++) {
        if(i == 0 && s.charAt(i) == '-') {
            if(s.length() == 1) return false;
            else continue;
        }
        if(Character.digit(s.charAt(i),radix) < 0) return false;
    }
    return true;
  }
}