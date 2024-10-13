import java.io.*;
import java.net.*;
import java.util.Scanner;
public class NW_EX6_TimeClient {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        try(Socket s = new Socket("localhost",12345))
        {
            System.out.println("Connected to server");
            System.out.println("Stop, Exit, Time");
            String msg;
            PrintWriter pw = new PrintWriter(s.getOutputStream(),true);
            BufferedReader bf = new BufferedReader(new InputStreamReader(s.getInputStream()));
            while (true) 
            {
              System.out.println("Enter your choice :  ");
              msg=inp.next();
              if(msg.equalsIgnoreCase("stop")|| msg.equalsIgnoreCase("exit"))
              {
                System.out.println("Exiting the connection");
                break;
              }
              else
              {
                System.out.println("Sneing request....");
                pw.println(msg);
                String rply = bf.readLine();
                System.out.println("MSG FROM SERVER \n___________________________________");
                System.out.println(rply);
              }
            }
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
    
}
