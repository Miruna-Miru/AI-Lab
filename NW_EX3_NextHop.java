import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.regex.*;

public class NW_EX3_NextHop {

  public static void main(String[] args) {
    try{
        String ip="",mac="",line;
        Process ipConfigPaProcess = Runtime.getRuntime().exec("ipconfig");
        Pattern ipPattern = Pattern.compile("\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b");
        BufferedReader bf = new BufferedReader(new InputStreamReader(ipConfigPaProcess.getInputStream()));
        while ((line=bf.readLine())!=null)
        {
                 if (line.contains("Default Gateway"))
                 {
                    Matcher match = ipPattern.matcher(line);
                    if(match.find())
                    {
                        ip=match.group();
                        break;
                    }
                 }
       }
       if(!ip.isEmpty())
       {
        System.out.print("Ip is : "+ip);
        Process arppProcess = Runtime.getRuntime().exec("arp -a");
        BufferedReader br = new BufferedReader(new InputStreamReader(arppProcess.getInputStream()));
        Pattern macPattern = Pattern.compile("([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})");
        while ((line=br.readLine())!=null) 
        {
            if(line.contains("Default gateway"))
            {
                   Matcher mm = macPattern.matcher(line);
                   if(mm.find())
                   {
                    mac=mm.group();
                    break;
                   }  
  
            }
            
        }
        if(!mac.isEmpty())
        System.out.print("mac is : "+mac);
        else
        System.out.println("No mac");
       }
       else
       System.out.print("No DG found");
    }
    catch(Exception e)
    {
        System.out.print(e.getMessage());
    }
  }
}