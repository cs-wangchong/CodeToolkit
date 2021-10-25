// verify file

class Foo {
    MessageDigest md;
    {
        md = MessageDigest.getInstance("MD5");
    }

    @override
    void foo() {
        MessageDigest md = MessageDigest.getInstance("MD5");
        try (InputStream is = Files.newInputStream(Paths.get("file.txt"));
            DigestInputStream dis = new DigestInputStream(is, md)) 
        {
        /* Read decorated stream (dis) to EOF as normal... */
        }
        byte[] digest = md.digest();
    }
}