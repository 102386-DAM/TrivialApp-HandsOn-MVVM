package cat.udl.tidic.amd.trivial.views;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

import cat.udl.tidic.amd.trivial.R;

public class DashboardActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);
    }

    public void startGame(View view){
        Log.d(this.getClass().getSimpleName(), " Navigate to "
                + GameActivity.class.getSimpleName());
        Intent intent = new Intent(this, GameActivity.class);
        startActivity(intent);
    }




}
