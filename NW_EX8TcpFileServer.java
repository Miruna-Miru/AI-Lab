import java.io.*;
import java.net.*;
public class NW_EX8TcpFileServer {
    public static void main(String[] args) {
        
        try(ServerSocket ss = new ServerSocket(12345))
        {
            System.out.println("Server started on port 12345");
            Socket s = ss.accept();
            System.out.println("Client connected");
            BufferedReader bf = new BufferedReader(new InputStreamReader(s.getInputStream()));
            PrintWriter pw = new PrintWriter(s.getOutputStream(),true);
            String msg;
            while(true)
            {
                msg=bf.readLine();
                if(msg.equalsIgnoreCase("stop"))
                {
                    System.out.println("terminating the connection..........");
                    break;
                }
                else
                {
                    File file = new File(msg);
                    if(!file.isDirectory() && file.exists())
                    {
                        System.out.println("File FOund on server");
                        pw.println("File found on server");
                        BufferedInputStream bis = new BufferedInputStream(new FileInputStream(file));
                        OutputStream os = s.getOutputStream();
                        byte buffer[] = new byte[4090];
                        int bytesread;
                        while((bytesread=bis.read(buffer))!=-1)
                          os.write(buffer,0,bytesread);
                        System.out.println("File sent....");
                       
                    }
                    else{
                     System.out.println("NO match found");
                    pw.println("no match");
                    }              
                }
            }
            bf.close();
            pw.flush();
            
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
