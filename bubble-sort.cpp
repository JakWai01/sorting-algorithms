int array[] = {9,8,7,3,6,1,2};

for (int i = 0; i < sizeof(array)/sizeof(array[0]); i++) {
    for (int j = 0; j < sizeof(array)/sizeof(array[0])-1; j++) {
        if (array[j] > array[j+1]) {
            swap(array[j],array[j+1]);
        }
    }
}

for (int i : array){
    cout << i;
}
