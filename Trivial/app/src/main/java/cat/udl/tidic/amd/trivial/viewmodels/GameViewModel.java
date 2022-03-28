package cat.udl.tidic.amd.trivial.viewmodels;

import androidx.lifecycle.MutableLiveData;

public class GameViewModel {
    public MutableLiveData<Integer> cat1;
    public MutableLiveData<Integer> cat2;
    public MutableLiveData<Integer> cat3;
    public MutableLiveData<Integer> cat4;

    public GameViewModel(){
        cat1 = new MutableLiveData<>();
        cat2 = new MutableLiveData<>();
        cat3 = new MutableLiveData<>();
        cat4 = new MutableLiveData<>();
    }
}