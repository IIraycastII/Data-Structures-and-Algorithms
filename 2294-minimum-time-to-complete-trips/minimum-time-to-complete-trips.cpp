class Solution {
public:
    long long checkTrips(vector<int> time, long long mid){
        long long total = 0;
        for (int i = 0 ; i < time.size(); i++){
            total += mid/time[i];
        }
        return total;
    }
    long long findMax(vector<int>& arr){
        long long maxVal;
        for(int i =0 ; i< arr.size(); i++){
            long long temp = (long long) arr[i];
            maxVal = max(temp, maxVal);
        }
        return maxVal;
    }
    long long minimumTime(vector<int>& time, int totalTrips) {
        long long low = 1, high = totalTrips * findMax(time);
        long long result = -1;
        while (low <= high){
            long long mid = (low+high)/2;
          
            if (checkTrips(time, mid)>=(long long)totalTrips){
                result = mid;
                high = mid -1;
            }
            else low = mid +1;
        }
        return result;
    }
};