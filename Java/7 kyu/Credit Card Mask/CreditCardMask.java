public class Maskify {
    public static String maskify(String str) {
        if(str.length() > 4) {
            String hash = new String(new char[str.length() - 4]).replace("\0", "#");
            return hash + str.charAt(str.length() - 4) + str.charAt(str.length() - 3) + str.charAt(str.length() - 2) + str.charAt(str.length() - 1);
        }
        else return str;
    }
}