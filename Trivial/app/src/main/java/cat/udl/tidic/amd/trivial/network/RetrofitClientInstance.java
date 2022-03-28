package cat.udl.tidic.amd.trivial.network;

import okhttp3.Call;
import okhttp3.OkHttpClient;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RetrofitClientInstance {

    private static Retrofit retrofit;
    private static final String BASE_URL = "http://10.0.2.2:8000";
    private static OkHttpClient client = new OkHttpClient.Builder()
            .build();

     public static Retrofit getRetrofitInstance() {
        if (retrofit == null) {
            retrofit = new retrofit2.Retrofit.Builder()
                    .baseUrl(BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .callFactory((Call.Factory) client)
                    .build();
        }
        return retrofit;
    }
}
