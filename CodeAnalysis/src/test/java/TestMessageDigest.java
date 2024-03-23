import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.Provider;
import java.security.Security;

public class TestMessageDigest{
    public static void main(String[] args) throws NoSuchAlgorithmException {
        for (Provider provider : Security.getProviders()) {
            System.out.println("Provider: " + provider.getName());
            for (Provider.Service service : provider.getServices()) {
                System.out.println("  Algorithm: " + service.getAlgorithm());
            }
        }

        MessageDigest md = MessageDigest.getInstance("whirlpool");
        md.update("aaaaaaa".getBytes(StandardCharsets.UTF_8));
        byte[] bytes = md.digest();
        final StringBuilder sb = new StringBuilder();
        for (int i = 0; i < bytes.length; i++) {
            sb.append(String.format("%02X", bytes[i]));
        }
        String hex = sb.toString().toLowerCase();
        System.out.println(hex);
    }
}
