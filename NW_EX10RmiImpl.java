import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class NW_EX10RmiImpl extends UnicastRemoteObject implements NW_EX10RmiInterface {
    private static final long serialVersionUID = 1L;

    // Explicit constructor
    public NW_EX10RmiImpl() throws RemoteException {
        super(); // Call the superclass constructor
    }

    @Override
    public void show() throws RemoteException {
        System.out.println("Hello! This is sample RMI code~~~");
    }
}
