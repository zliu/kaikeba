

int arr[];


// empty array :  max_sum is 0
// one element array: max_sum is this element
// two element array:  max_sum is the bigger one of the elements
// three :  compare [0]+[2] and [1] 


[ _, _ ]
a = [ x, _ ]
b = [ -, x ]

[ _, _, _ ]
a' = [ x, _, x ]
b' = [ _, x, _ ]

[ _, _, _, _ ]
a'' = [ x, _, x, _ ]
[ x, _, _, x ]
[ _, x, _, x ]
[ _, x, _, _ ]
[ _, _, x, _ ]
[ _, _, _, x ]

int max_sum(int *array, int size){
    // if there is only one element
    if (size == 0){
        return 0;
    } else if (size == 1){
        return array[0];    
    } else if (size ==2){
        return array[0] >= array[1] ? array[0]:array[1];
    } else {

        // if the one before last is picked
        int last_one_picked = max_sum(array, size-1);
        // else 
        int last_one_not_picked = max_sum(array, size-1) + array[size-1];
    
        return last_one_picked >= last_one_not_picked ? last_one_picked:last_one_not_picked;
    }

}