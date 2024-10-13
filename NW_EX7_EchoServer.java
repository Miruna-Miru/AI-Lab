import java.io.*;
import java.net.*;

public class NW_EX7_EchoServer {
    public static void main(String[] args) {
        try(ServerSocket ss = new ServerSocket(12345))
        {
            System.out.println("Server started on port :  12345");
            Socket s = ss.accept();
            System.out.println("Client connected");
            BufferedReader bf = new BufferedReader(new InputStreamReader(s.getInputStream()));
            PrintWriter pw = new PrintWriter(s.getOutputStream(),true);
            String msg;
            while((msg=bf.readLine())!=null)
            {
              if(msg.equalsIgnoreCase("stop"))
              {
                System.out.println("Terminating the connection");
                break;
              }    
              else
              {
                System.out.println("From CLIET : "+msg);
                pw.println("---->"+msg);
              }
            }
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
       
    }
}
