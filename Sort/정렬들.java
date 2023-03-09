package Sort;

import java.util.Arrays;
import java.util.Random;

public class 정렬들{
    public static void main(String[] args) {
        System.out.println("asd");
        
        int[] randomIntArr = new int[100];
        
        createRandInt(randomIntArr);
        // System.out.println("---- Selection Sort ----");
        // bubbleSort(randomIntArr);

        System.out.println("---- Selection Sort ----");
        SelectionSort(randomIntArr);

        System.out.println(Arrays.toString(randomIntArr));
    }
    
    static void createRandInt(int[] arr){
        Random rand = new Random();

        for(int i = 0; i < arr.length; i++){
            arr[i] = rand.nextInt() % 100;
        }
    }
    
    static void bubbleSort(int[] arr){
        for(int i = 0; i < arr.length; i++){
            for(int j = 0; j < arr.length - i -1; j++){
                if( arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }

    static void SelectionSort(int[] arr){
        for(int i = 0; i < arr.length-1; i++){
            int indexMin = i;
            for(int j=i+1; j<arr.length; j++){
                if(arr[indexMin] > arr[j]){
                    indexMin = j;
                }
            }
            
            int temp = arr[i];
            arr[i] = arr[indexMin];
            arr[indexMin] = temp;
        }
    }
}
