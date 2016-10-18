import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class sol {
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line;
        while ((line = br.readLine()) != null)
        {
            String[] toks = line.split(" ");

            long a = Long.parseLong(toks[0]);
            long b = Long.parseLong(toks[1]);

            System.out.println(Math.abs(a-b));
        }
    }

}
