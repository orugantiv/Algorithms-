class MergeSort:
    def __init__(self,arr):
        self.arr = arr;
        self.sort(self.arr);

    def sortTwoSet(self, 
                    arr, 
                    left_arr, 
                    right_arr,
                    i,
                    j,
                    k):
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i+=1
                else:
                    arr[k] = right_arr[j]
                    j+=1;
                k+=1
            return (i,j,k)

    def sortSingleSet(self, arr, temp_arr, index_i, index_k):
            while index_i < len(temp_arr):
                arr[index_k] = temp_arr[index_i];
                index_i+=1
                index_k+=1
  
    def sort(self, arr):
        if len(arr) >1:
            left_arr = arr[:len(arr)//2]
            right_arr = arr[len(arr)//2:]
            self.sort(left_arr);
            self.sort(right_arr);
            (i,j,k)=(0,0,0)
            (i,j,k) = self.sortTwoSet(arr,left_arr, right_arr,i,j,k)
            self.sortSingleSet(arr,left_arr, i,k)
            self.sortSingleSet(arr, right_arr, j,k)



if __name__ == "__main__":            
    arr_tes = ([2,3,5,1,7,4,4,4,2,6,0]);
    MergeSort(arr_tes);
    print(f"{arr_tes}")


