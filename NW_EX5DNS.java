import java.util.Scanner;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.util.Enumeration;

public class NW_EX5DNS {

    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        resolveLocalDNS();
        System.out.print("Enter domain nem : ");
        String dn = inp.next();
        resolveDomain(dn);
    }

    static void resolveLocalDNS()
    {
        try
        {
            Enumeration<NetworkInterface> nwIfs= NetworkInterface.getNetworkInterfaces();
            while (nwIfs.hasMoreElements()) 
            {
               NetworkInterface nw = nwIfs.nextElement();
               Enumeration<InetAddress> inet = nw.getInetAddresses();
               while(inet.hasMoreElements())
               {
                InetAddress ip = inet.nextElement();
                System.out.println("Interface   :  "+nw.getName());
                System.out.println("IP          :  "+ip.getHostAddress());
                System.out.println("Host name :  "+ip.getHostName());
               }    
            }
        }
        catch(Exception e){
        System.out.println(e.getMessage());
        }
    }

  static  void resolveDomain(String dn)
    {
        try
        {
            InetAddress ip = InetAddress.getByName(dn);
            System.out.println("Ip       :  "+ip.getHostAddress());
        }
        catch(Exception e)
        {
            System.out.print(e.getMessage());
        }
    }
}