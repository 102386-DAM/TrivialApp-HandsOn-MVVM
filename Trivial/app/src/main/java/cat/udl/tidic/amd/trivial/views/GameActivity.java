package cat.udl.tidic.amd.trivial.views;

import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.databinding.DataBindingUtil;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;

import cat.udl.tidic.amd.trivial.R;
import cat.udl.tidic.amd.trivial.databinding.ActivityGameBinding;
import cat.udl.tidic.amd.trivial.models.Category;
import cat.udl.tidic.amd.trivial.viewmodels.GameViewModel;

public class GameActivity extends AppCompatActivity {

    ActivityGameBinding activityGameBinding;
    GameViewModel viewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        initDataBinding();
        initLayout();

    }

    private void initDataBinding() {
        activityGameBinding= DataBindingUtil.setContentView(this, R.layout.activity_game);
        // Required to update UI with LiveData
        viewModel = new GameViewModel();
        activityGameBinding.setGameViewModel(viewModel);
        activityGameBinding.setLifecycleOwner(this);
    }

    private void initLayout(){

        activityGameBinding.cat1Img.setBackground(ContextCompat.getDrawable(
                getApplicationContext(),Category.db.getColor()
        ));
        activityGameBinding.cat1TV.setText(Category.db.toString());
        viewModel.cat1.setValue(0);


        activityGameBinding.cat2Img.setBackground(ContextCompat.getDrawable(
                getApplicationContext(),Category.os.getColor()
        ));
        activityGameBinding.cat2TV.setText(Category.os.toString());
        viewModel.cat2.setValue(0);

        activityGameBinding.cat3Img.setBackground(ContextCompat.getDrawable(
                getApplicationContext(),Category.patterns.getColor()
        ));
        activityGameBinding.cat3TV.setText(Category.patterns.toString());
        viewModel.cat3.setValue(0);

        activityGameBinding.cat4Img.setBackground(ContextCompat.getDrawable(
                getApplicationContext(),Category.net.getColor()
        ));
        activityGameBinding.cat4TV.setText(Category.net.toString());
        viewModel.cat4.setValue(0);

    }

    public void play(View view){
        Log.d(this.getClass().getSimpleName(), " Navigate to "
                + QuestionActivity.class.getSimpleName());
        Intent intent = new Intent(this, QuestionActivity.class);
        //startActivity(intent);
        questionActivityResultLauncher.launch(intent);
    }

    ActivityResultLauncher<Intent> questionActivityResultLauncher = registerForActivityResult(
            new ActivityResultContracts.StartActivityForResult(),
            new ActivityResultCallback<ActivityResult>() {
                @Override
                public void onActivityResult(ActivityResult result) {
                    if (result.getResultCode() == Activity.RESULT_OK) {
                        // There are no request codes
                        Intent data = result.getData();
                        Bundle b = new Bundle();
                        b = data.getExtras();
                        String cat = b.getString("cat");
                        Boolean isCorrect = b.getBoolean("isCorrect");

                        Log.d(this.getClass().getSimpleName(), ""+cat+"->"+isCorrect);

                        if (cat.equals(Category.db.toString()) && isCorrect){
                            viewModel.cat1.setValue(viewModel.cat1.getValue() + 1);
                        }
                        if (cat.equals(Category.os.toString()) && isCorrect){
                            viewModel.cat2.setValue(viewModel.cat2.getValue() + 1);
                        }
                        if (cat.equals(Category.patterns.toString()) && isCorrect){
                            viewModel.cat3.setValue(viewModel.cat3.getValue() + 1);
                        }
                        if (cat.equals(Category.net.toString()) && isCorrect){
                            viewModel.cat4.setValue(viewModel.cat4.getValue() + 1);
                        }
                    }
                }
            });




}