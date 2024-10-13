import java.io.*;
import java.net.*;
import java.time.*;
import java.time.format.DateTimeFormatter;

public class NW_EX6_TimeServer {
    public static void main(String[] args) {
        String msg="";
        try(ServerSocket ss = new ServerSocket(12345))
        {
            System.out.println("Server Started on port 12345");
            Socket s = ss.accept();
            System.out.println("Client connected!");
            BufferedReader bf = new BufferedReader(new InputStreamReader(s.getInputStream()));
            PrintWriter pw = new PrintWriter(s.getOutputStream(),true);
            while((msg=bf.readLine())!=null)
            {
                if(msg.equalsIgnoreCase("time"))
                {
                    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
                    String cr = LocalDateTime.now().format(formatter);
                    pw.println(cr);
                    System.out.println("Time sent to client");
                }
                else if (msg.equalsIgnoreCase("stop") || msg.equalsIgnoreCase("exit"))
                {
                    System.out.println("Server stoped connection");
                    break;
                }
                else
                {
                    System.out.println("Server recieved : "+msg);
                    pw.println("Unkown Request for time server ~!\nServer got : "+msg);
                }
            }
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
