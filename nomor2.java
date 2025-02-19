public class nomor2 {
    public static void main(String[] args) {
        int[] kodeBarang = {
            564, 123, 789, 345, 890, 234, 456, 678, 987, 654,
            342, 567, 876, 109, 876, 231, 567, 987, 321, 345,
            678, 234, 543, 678, 890, 123, 567, 890, 234, 567,
            789, 876, 109, 876, 231, 567, 987, 321, 345, 678,
            890, 123, 567
        };

        System.out.println("Data sebelum diurutkan:");
        printArray(kodeBarang);

        shellSort(kodeBarang);

        System.out.println("\nData setelah diurutkan:");
        printArray(kodeBarang);
    }

    public static void shellSort(int[] arr) {
        int n = arr.length;
        for (int gap = n / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < n; i++) {
                int temp = arr[i];
                int j;
                for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                    arr[j] = arr[j - gap];
                }
                arr[j] = temp;
            }
        }
    }

    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}