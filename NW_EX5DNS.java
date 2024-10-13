import java.net.InetAddress;
import java.net.UnknownHostException;


public class NW_EX5DNS {
    public static void main(String[] args) {
        try {
            
            InetAddress localHost = InetAddress.getLocalHost();
            System.out.println("Local Host IP: " + localHost.getHostAddress());
            System.out.println("Local Host Name: " + localHost.getHostName());

      
            String domainName = "google.com"; 
            InetAddress[] inetAddresses = InetAddress.getAllByName(domainName);

            System.out.println("IP Addresses for domain " + domainName + ": ");
            for (InetAddress addr : inetAddresses) {
                System.out.println(addr.getHostAddress());
            }
        } catch (UnknownHostException e) {
            System.out.println("Error resolving domain: " + e.getMessage());
        }
    }
}
