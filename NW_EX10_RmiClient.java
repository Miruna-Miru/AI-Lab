import java.rmi.Naming;
public class NW_EX10_RmiClient {
    public static void main(String[] args) {
        try{
        NW_EX10RmiInterface manager = (NW_EX10RmiInterface) Naming.lookup("rmi://localhost/RMIexam");
        manager.show();
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
