import java.io.BufferedReader;
import java.io.InputStreamReader; 
 
public class NetworkUtils { 
 
    public static void main(String[] args) { 
        try { 
            String hostname = "www.google.com";  
            String nextHopIp = getNextHopIp(hostname); 
            String macAddress = getMacAddress(nextHopIp); 
 
            System.out.println("Next Hop IP: " + nextHopIp); 
            System.out.println("MAC Address: " + macAddress); 
        } catch (Exception e) { 
            e.printStackTrace(); 
        } 
    } 
    private static String getNextHopIp(String hostname) throws Exception { 
        String command = System.getProperty("os.name").toLowerCase().contains("win") ? "tracert" : "traceroute"; 
        ProcessBuilder pb = new ProcessBuilder(command,hostname); 
        Process process = pb.start();
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream())); 
        String line; 
        while ((line = reader.readLine()) != null) { 
            if (line.contains("ms")) {  
                String[] parts = line.split("\\s+"); 
                return parts[parts.length - 1];  
            } 
        } 
        return null; 
    } 
    private static String getMacAddress(String ip) throws Exception { 
        ProcessBuilder pb = new ProcessBuilder("arp", "-a"); 
        Process process = pb.start(); 
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream())); 
        String line; 
        while ((line = reader.readLine()) != null) { 
            if (line.contains(ip)) { 
                String[] parts = line.split("\\s+"); 
                return parts[2];  
            } 
        } 
        return null; 
    } 
}