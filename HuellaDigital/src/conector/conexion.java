/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conector;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.request.body.MultipartBody;
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;

public class conexion {

    private Connection Con;
    //private final String url = "jdbc:mysql://localhost:3306/control_asistencia";
    private final String url = "jdbc:mysql://190.121.135.167:4005/control_asistencia";
    private final String user = "root";

    public conexion() {
        Conectar();
    }

    public void Conectar() {

        try {
            Class.forName("com.mysql.jdbc.Driver");
            Con = DriverManager.getConnection(url, user, "lilamelendez");
            System.out.println("Conectado");

        } catch (Exception e) {

            System.out.println("No se ha establecido conexión" + e);

        }
    }

    public Connection getConexion() {
        return Con;
    }

    public void Desconectar() {
        Con = null;
    }

    public static void main(String[] args) {
        //  conexion con = new conexion();
        try {
            /*HttpResponse<String> response = Unirest.post("https://frigosinu.andrea.com.co/lila/api/turnos/1")
                    .header("Content-Type", "multipart/form-data;").header("Acept", "application/json")
                    .asString();*/
            File file = new File(".\\src\\imagenes\\foto.jpg");
           /* MultipartBody response = Unirest.post("http://192.168.1.17:3000/api/turnos/1")
                    //.header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
                    .field("imagen", file);*/
            String url = "http://192.168.1.17:3000";
            MultipartBody response = Unirest.post(url + "/api/turnos/1")
                    .field("imagen", file);

            System.out.println(response.asString().getBody()+ "");
            /*  URL url = new URL("https://postman-echo.com/post");
            String postData = "foo1=bar1&foo2=bar2";

            URLConnection conn = url.openConnection();
            conn.setDoOutput(true);
            conn.setRequestProperty("Content-Type", "application/json");
           

            DataOutputStream dos = new DataOutputStream(conn.getOutputStream());
            dos.writeBytes(postData);

            BufferedReader bf = new BufferedReader(new InputStreamReader(
                    conn.getInputStream()));

            String line;
            while ((line = bf.readLine()) != null) {
                System.out.println(line);
            }*/

        } catch (Exception e) {
        }
    }

}
