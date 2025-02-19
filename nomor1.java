public class nomor1 {
    public static void main(String[] args) {
        int[] nilaiUjian = {78, 92, 45, 67, 88, 61, 95, 74, 83, 56};
        
        System.out.println("Daftar Nilai Awal:");
        displayArray(nilaiUjian);
        
        // Proses pengurutan dengan Bubble Sort
        bubbleSort(nilaiUjian);
        
        System.out.println("\nDaftar Nilai Setelah Diurutkan:");
        displayArray(nilaiUjian);
    }
    
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;
        
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Tukar nilai
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            
            // Jika tidak ada pertukaran dilakukan pada iterasi ini, maka array sudah terurut
            if (!swapped) {
                break;
            }
            
            // Tampilkan proses setiap langkah
            System.out.println("\nLangkah " + (i + 1) + ":");
            displayArray(arr);
        }
    }
    
    public static void displayArray(int[] arr) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}
