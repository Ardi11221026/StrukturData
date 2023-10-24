import java.util.Random;

public class InsertionSort {
    public static void main(String[] args) {
        int[] arr = generateRandomArray(10);
        System.out.println("Array sebelum diurutkan:");
        printArray(arr);

        insertionSort(arr);

        System.out.println("\nArray setelah diurutkan:");
        printArray(arr);
    }

    // Fungsi untuk menghasilkan array angka acak dari 1 sampai 100 tanpa ada angka yang sama
    public static int[] generateRandomArray(int length) {
        if (length > 100) {
            System.out.println("Panjang array tidak boleh lebih dari 100.");
            return null;
        }

        int[] arr = new int[length];
        Random rand = new Random();
        for (int i = 0; i < length; i++) {
            int num;
            do {
                num = rand.nextInt(100) + 1; // Menghasilkan angka acak dari 1 sampai 100
            } while (contains(arr, num)); // Pastikan angka belum ada dalam array
            arr[i] = num;
        }
        return arr;
    }

    // Fungsi untuk mengecek apakah sebuah angka sudah ada dalam array
    public static boolean contains(int[] arr, int num) {
        for (int i : arr) {
            if (i == num) {
                return true;
            }
        }
        return false;
    }

    // Fungsi untuk mengurutkan array menggunakan Insertion Sort
    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;

            // Pindahkan elemen dari arr[0..i-1] yang lebih besar dari key
            // ke satu posisi di depan posisinya saat ini
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }

    // Fungsi untuk mencetak array
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
