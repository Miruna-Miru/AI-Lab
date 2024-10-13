import java.io.*;
import java.net.*;
import java.util.Scanner;
public class NW_EX7_EchoClient 
{
    public static void main(String[] args) 
    {
        Scanner inp = new Scanner(System.in);
        try(Socket s = new Socket("localhost",12345))
        {
            BufferedReader bf = new BufferedReader(new InputStreamReader(s.getInputStream()));
            PrintWriter pw = new PrintWriter(s.getOutputStream(),true);
            s.setSoTimeout(5000); 
            Thread ping = new Thread(() -> {
               try
               {
                while(true)
                {
                 pw.println("Ping");
                 String l= bf.readLine();
                 if(!l.isEmpty())
                 System.out.println("Ping from server : "+l);
                 else{
                    System.out.println("No reply from server.....Exiting");
                    break;
                 }
                 Thread.sleep(5000); 
                }
                }
                catch (Exception e)
                {
                    System.out.println(e.getMessage());
                }
            });
            ping.start();
            while (true)
             {
               System.out.println("Enter msg  : ");
               String msg = inp.next();
               pw.println(msg);
               String rply = bf.readLine();
               System.out.println("from Server..  "+rply);
               if(msg.equalsIgnoreCase("stop"))
               {
                System.out.println("Exiting.........");
                break;
               }
            }
            
        }catch(Exception ee)
        {
            System.out.println(ee.getMessage());
        }
    }
}
