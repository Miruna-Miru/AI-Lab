import java.util.Scanner;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;

public class NW_EX4_PortScanner {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        try
        {
          InetAddress localHost = InetAddress.getLocalHost();
          String ip=localHost.getHostAddress();
          System.out.print("Enter starting and ending port :  ");
          int st=inp.nextInt();
          int end=inp.nextInt();
          System.out.println("Scanning on : "+ip);
          for(int i=st;i<=end;i++)
          {
            try
            {
                Socket ss=new Socket(ip,i);
                System.out.println("Opened port :  "+i);
                ss.close();
            }
            catch(IOException e)
            {
                
            }
          }
        }
        catch(Exception ww)
        {
            System.out.print(ww.getMessage());
        }
    }
}
