public class StringCompression{
    
    public static String compress(String ip){
        String op="";
        int i=0,j=0,count=1;
       
            
            for(i=1;i<ip.length();i++){
                System.out.println(ip.charAt(i)==ip.charAt(j));
                if(ip.charAt(i)==ip.charAt(j)){
                    count++;
                    
                }
                else{ op=op+ip.charAt(j)+""+count;
                count=1;
                j=i;
                    
                }
            }
            op=op+ip.charAt(j)+""+count;
                
                
System.out.println(op);
            
        return op.length()<ip.length()?op:ip;
        
    }
     public static void main(String []args){
        System.out.println(compress("aabcccccaaa"));
        
     }
}