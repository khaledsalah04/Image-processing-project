package com.myfinalnewclientserverapp.com;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.util.Base64;

import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;
import java.net.UnknownHostException;

public class sendMessage extends AsyncTask<Bitmap , Void , Bitmap>{


    @Override
    protected Bitmap doInBackground(Bitmap... bitmaps) {

        try {

            try {

                Socket socket = new Socket("192.168.1.5", 8888);

                ByteArrayOutputStream stream = new ByteArrayOutputStream();
                Bitmap bitmapimg = bitmaps[0];
                bitmapimg = Bitmap.createScaledBitmap(bitmapimg, 200, 200, true);
                bitmapimg.compress(Bitmap.CompressFormat.PNG, 100, stream);
                byte[] byteArray = stream.toByteArray();
                String encodedImage = Base64.encodeToString(byteArray, Base64.DEFAULT);
                byte[] byteArray2 = Base64.encode(byteArray, Base64.DEFAULT);

                DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
                int size = byteArray2.length;
                //dos.write(byteArray2.length);
                dos.write(byteArray2);

                dos.flush();
                dos.close();
                socket.close();
/////////////////////////////////////////////////////////////////////////////////////////////////////

                Socket socket1 = new Socket("192.168.1.5",8888);
                InputStream in = socket1.getInputStream();
                ByteArrayOutputStream bos = new ByteArrayOutputStream(1024);
                byte[] buff = new byte[1024];
                int numBytesJustRead =0;

                while (true)
                {
                    int n = in.read(buff);

                    if(n<0)
                    {
                        break;
                    }
                    bos.write(buff,0,n);


                }

                byte [] b = bos.toByteArray();
                bos.close();
                socket1.close();

/*                String s = new String(b);

                return  s;
*/

                byte [] bb = Base64.decode(b,Base64.DEFAULT);
                Bitmap translated_img = BitmapFactory.decodeByteArray(bb, 0, bb.length);
                int x =0;
                return translated_img;


            } catch (UnknownHostException e) {
                e.printStackTrace();
            }
        }catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
}
