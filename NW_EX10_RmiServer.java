import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;
public class NW_EX10_RmiServer {
    public static void main(String[] args) {
        try{
           NW_EX10RmiImpl manger = new NW_EX10RmiImpl();
           LocateRegistry.createRegistry(1099);
           Naming.rebind("RMIexam", manger);
           System.out.println("Server RMI is ready");

        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
    
}
