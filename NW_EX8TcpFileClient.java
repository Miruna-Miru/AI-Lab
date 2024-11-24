import java.util.Scanner;
import java.io.*;
import java.net.*;

public class NW_EX8TcpFileClient {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        try(Socket s = new Socket("localhost",12345))
        {
           System.out.println("Connected to SERVER...");
           BufferedReader bf = new BufferedReader(new InputStreamReader(s.getInputStream()));
           PrintWriter pw = new PrintWriter(s.getOutputStream(),true);
           String msg;
           while(true)
           {
              System.out.print("Enter file nmae:  ");
              msg=inp.next();
              if(msg.equalsIgnoreCase("stop"))
              {
                System.out.println("Terminating the connection.........");
                break;
              }
              else
              {
                String rply;
                pw.println(msg);
                rply=bf.readLine();
                if(rply.equalsIgnoreCase("no match"))
                {
                    System.out.println(rply);
                }
                else
                {
                    System.out.println(rply);
                    System.out.println("Enter new file name : ");
                    String nf = inp.next();
                    InputStream is = s.getInputStream();
                    BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(nf));
                    byte [] buffer = new byte[4090];
                    int bytesread;
                    while((bytesread=is.read(buffer))!=-1)
                      bos.write(buffer,0,bytesread);
                    System.out.println("File saved!!!!!!!!!!");
                    bos.close();
                    is.close();

                }
              }
           }
            bf.close();
            pw.close();
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
        inp.close();
    }
}
