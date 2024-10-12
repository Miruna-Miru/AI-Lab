import java.net.InetAddress;
import java.util.Scanner;

public class NW_EX2_Hostname {

    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        System.out.print("Enter domain name : ");
        String dn = inp.nextLine();
        try{
        InetAddress ia = InetAddress.getByName(dn);
        System.out.print("Host name : "+ia.getHostName());
        System.out.print("\nHost address : "+ia.getHostAddress()); 
        System.out.print("\nTHis system's Info : \n");
        InetAddress iaa = InetAddress.getLocalHost();
        System.out.print("Host name : "+iaa.getHostName());
        System.out.print("\nHost address : "+iaa.getHostAddress());
        }
        catch (Exception e){
            System.out.println(e.getMessage());
        }
    }
}