/*
 * @author Soniya Rode
 * Code to find the smallest positive integer not present in an unsorted array.
 * 
 */
import java.util.*;

public class Solution {
        public static int solution(int[] A) {
        // First sort the array
        Arrays.sort(A);
        
        //Find the index of first positive element in the array
        int i=0;
        while( A[i]<=0){

                i++;
                if(i>=A.length){
                    return 1;

                }
        }
        

        //If the first positivie element is >1 return 1
        int min=1;
        if(A[i]>min){
            return min;
        }
        
        //else traverse the array till difference between adjacent number is >1
       int j=i;
       
        while(j<A.length-1){
          if(Math.abs(A[j]-A[j+1])>1){
              min=A[j]+1;
              break;
          }
          j++;
        }
        if(j==A.length -1){
            min=A[j]+1;
            
        }
        return min;
        
    }

  public static void main(String args[]){
      int a[]={ -1,-3,1,2,4};
      System.out.println(solution(a));
      
  }
}