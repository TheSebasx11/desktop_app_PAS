/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package clases;

import java.sql.Connection;
import java.sql.DriverManager;

public class conexion {

    private Connection Con;
    private final String url = "jdbc:mysql://localhost:3306/control_asistencia";
    private final String user = "root";

    public conexion() {
        Conectar();
    }

    public void Conectar() {

        try {
            Class.forName("com.mysql.jdbc.Driver");
            Con = DriverManager.getConnection(url, user, "");
            System.out.println("Conectado");

        } catch (Exception e) {
            System.out.println("No se ha establecido conexión");

        }
    }

    public Connection getConexion() {
        return Con;
    }

    public void Desconectar() {
        Con = null;
    }

    public static void main(String[] args) {
        conexion con = new conexion();
    }

}
