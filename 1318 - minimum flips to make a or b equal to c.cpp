class Solution {
public:
    int minFlips(int a, int b, int c) {
        int bitsum = (a|b);
        int count = 0;
        int bitmask = 1;
        // bitsum|c = a|b|c, must be >= max(a,b,c)
        while(bitmask <= (bitsum | c)){
            if((bitsum & bitmask) != (c & bitmask)){
                if((bitsum & bitmask) == 0){
                    count += 1;
                } else{
                    if((a & bitmask) == 0 || (b & bitmask) == 0){
                        count += 1;
                    }
                    else{
                        count += 2;
                    }
                }
            }
            bitmask<<=1;
        }
        return count;
    }
};