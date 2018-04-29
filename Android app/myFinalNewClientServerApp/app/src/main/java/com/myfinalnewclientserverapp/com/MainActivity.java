package com.myfinalnewclientserverapp.com;

import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.provider.MediaStore;
import android.support.v4.graphics.BitmapCompat;
import android.support.v7.app.AppCompatActivity;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.ByteArrayOutputStream;
import java.util.concurrent.ExecutionException;

public class MainActivity extends AppCompatActivity {

    private ImageView mImageView;
    static final int REQUEST_TAKE_PHOTO = 1;
    private Button button;
    private Bitmap imageBitmap;
    private TextView textView;
    private int TARGET_LANGUAE = 0 ;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



        button = (Button) findViewById(R.id.button);
        mImageView = (ImageView) findViewById(R.id.imageView);
        textView = (TextView) findViewById(R.id.textView);



        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String tranlation = null;
               sendMessage s =  new sendMessage();

                try {

                    tranlation = s.execute(imageBitmap).get();

                    //imageBitmap =  s.execute(imageBitmap).get();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (ExecutionException e) {
                    e.printStackTrace();
                }

                //mImageView.setImageBitmap(imageBitmap);
                textView.setText(tranlation);
            }
        });
    }

    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu, menu);
        return true;
    }


    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()){

            case R.id.arabic:

                TARGET_LANGUAE =1;
                return true;

            case R.id.french:

                TARGET_LANGUAE =2;
                return true;

            case R.id.german:

                TARGET_LANGUAE =3;
                return true;

            case R.id.english:

                TARGET_LANGUAE =4;
                return true;

            default:

                TARGET_LANGUAE =0;
                return super.onOptionsItemSelected(item);

        }
    }

    public void startCamera(View view) {
        dispatchTakePictureIntent();
    }

    static final int REQUEST_IMAGE_CAPTURE = 1;

    private void dispatchTakePictureIntent() {
        Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
            startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE);
        }
    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQUEST_TAKE_PHOTO && resultCode == RESULT_OK) {
            Bundle extras = data.getExtras();
            imageBitmap = (Bitmap) extras.get("data");
            mImageView.setImageBitmap(imageBitmap);
            int bitmapByteCount = BitmapCompat.getAllocationByteCount(imageBitmap);


            ByteArrayOutputStream stream = new ByteArrayOutputStream();
            imageBitmap.compress(Bitmap.CompressFormat.PNG, 100, stream);
            byte[] byteArray = stream.toByteArray();

            //     imageBitmap.recycle();
        }
    }



}