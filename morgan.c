

int array[] = [1,2,3];
int sub[] = [1,3];

bool is_sub(array, sub)
{
    int array_len = sizeof(array)/sizeof(array[0]);
    int sub_len = sizeof(sub)/sizeof(sub[0]);
    bool match = false;
    int matched = 0;
    for (int i= 0; i<sub_len; i++){
        for (int j =0 ; j<array_len-sub_len; j++){
            if(array[j] == sub[i]){
                matched + =1;

                continue;
            }
        }
        
    }





    for (int i =0; i< array_len-sub_len; i++)
    {
        bool nomatch = false;
        for (int j = 0; j< sub_len; j++)
        {
            if(sub=[j] != array[i+j])
            {
                break;
                nomatch = true;
            }
        }
        if(j == sub_len -1 && !nomatch)
        {
            match = true;
            break;
        }
    }
    return match;
    if(match)
      return true;
    else
      return false;
}