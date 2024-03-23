package srctoolkit.janalysis.hash;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
//        String[] tokens1 = new String[]{"Bitmap", "image", "=", "BitmapFactory", ".", "decodeStream", "(", "input", ")", ";"};
//        String[] tokens2 = new String[]{"Bitmap", "bmp", "=", "BitmapFactory", ".", "decodeStream", "(", "is", ",", "null", ",", "options", ")", ";"};
        String[] tokens1 = new String[]{"Bitmap", "#", "=", "BitmapFactory", ".", "decodeStream", "(", "#", ")", ";"};
        String[] tokens2 = new String[]{"Bitmap", "#", "=", "BitmapFactory", ".", "decodeStream", "(", "#", ",", "#", ",", "#", ")", ";"};
        String[] twoGram1 = new String[tokens1.length - 1];
        for (int i = 0; i < tokens1.length - 1; i++) {
            twoGram1[i] = tokens1[i] + " " + tokens1[i + 1];
        }
        String[] twoGram2 = new String[tokens2.length - 1];
        for (int i = 0; i < tokens2.length - 1; i++) {
            twoGram2[i] = tokens2[i] + " " + tokens2[i + 1];
        }
        long hash1 = SimHash.simhash64(Arrays.asList(tokens1));
        long hash2 = SimHash.simhash64(Arrays.asList(tokens2));
        long hash3 = SimHash.simhash64(Arrays.asList(twoGram1));
        long hash4 = SimHash.simhash64(Arrays.asList(twoGram2));
        System.out.println(Long.toHexString(hash1));
        System.out.println(Long.toHexString(hash2));
        System.out.println(SimHash.hammingDistance(hash1, hash2));
        System.out.println(Long.toHexString(hash3));
        System.out.println(Long.toHexString(hash4));
        System.out.println(SimHash.hammingDistance(hash3, hash4));
        System.out.println(SimHash.hammingDistance(hash1, hash2) + SimHash.hammingDistance(hash3, hash4));
    }
}
