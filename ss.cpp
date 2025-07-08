#include <cstddef>
#include <utility>
#include <random>
#include <iostream>

using namespace std;


void selection_sort(int* arr, size_t _SIZE){
    for (size_t i = 1; i < _SIZE; i++) {
        for (size_t k = i; i > 0 && arr[k] > arr[k - 1]; k--) {
            std::swap(arr[k-1], arr[k]);
        }
    }
    
}

void printArray(int* arr, size_t _SIZE){
    for (size_t index = 0; index < _SIZE; index++)
    {
        cout << arr[index] << " ";
    }
}

int main(){
    const size_t _SIZE = 10;
    int * arr = new int[_SIZE];
    for (size_t i = 0; i < _SIZE; i++)
    {
        arr[i] = rand();
    }
    printArray(arr, _SIZE);
}