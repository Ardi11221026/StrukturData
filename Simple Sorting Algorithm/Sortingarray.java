import java.util.*;
public class Sortingarray {  
public static void main(String[] args) {  
   
    //deklarasi array dan print array awal
    int[] numArray = {48, 22, 6, 79, 11, 34, 67, 92, 15, 3, 51, 71, 14,
                    96, 59, 8, 50, 91, 28, 64, 18, 74, 35, 97, 40, 69,
                    26, 43, 75, 1, 38, 21, 87, 56, 17, 65, 9, 45, 30, 81,
                    42, 61, 12, 70, 55, 37, 86, 53, 25, 77, 29, 63, 7, 58,
                    46, 95, 20, 78, 49, 2, 83, 44, 73, 66, 32, 68, 5, 90,
                    19, 94, 47, 36, 10, 88, 60, 31, 76, 13, 85, 41, 84, 33,
                    72, 4, 22, 16, 54, 99, 24, 62, 57, 27, 89, 23, 80, 52,
                    82, 1, 100, 96};  

    System.out.println("Original Array: " + Arrays.toString(numArray));

    //mengaplikasikan insertion sort pada array
    for(int k=1; k<numArray.length; k++)   {  
        int temp = numArray[k];
        int j= k-1;  
        while(j>=0 && temp <= numArray[j])   {  
            numArray[j+1] = numArray[j];  
            j = j-1;  
        }  
        numArray[j+1] = temp;
    }  
    //print array setelah di sorting
    System.out.println("\nSorted Array: " + Arrays.toString(numArray));
    System.out.print("jumlah indeks array adalah = " +numArray.length);
} 
}