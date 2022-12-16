/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conector;

/**
 *
 * @author Sebastian
 */
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class Operaciones {

    private PreparedStatement st;
    private ResultSet rs;
    private String SelectUserCargo;
    private String SelectCargos;
     private String InsertUsuario;
    
    public Operaciones() {
        st = null;
        rs = null;
        SelectUserCargo = "SELECT usuarios.*, cargos.nombre as Nombre_Cargo FROM `usuarios`, cargos WHERE usuarios.cargo = cargos.id_cargo";
        SelectCargos = "SELECT * FROM cargos;";
          InsertUsuario = "INSERT INTO `usuarios`(`cargo`, `name_01`, `name_02`, `lastname01`, `lastname02`, `fecha_nac`, `identificacion`, `sexo`, `email`, `telefono`) VALUES (?,?,?,?,?,?,?,?,?,?)";
    }

    public String getSelectCargos() {
        return SelectCargos;
    }

    public void setSelectCargos(String SelectCargos) {
        this.SelectCargos = SelectCargos;
    }

    public String getInsertUsuario() {
        return InsertUsuario;
    }

    public void setInsertUsuario(String InsertUsuario) {
        this.InsertUsuario = InsertUsuario;
    }
    
    public PreparedStatement getSt() {
        return st;
    }

    public void setSt(PreparedStatement st) {
        this.st = st;
    }

    public ResultSet getRs() {
        return rs;
    }

    public void setRs(ResultSet rs) {
        this.rs = rs;
    }

    public String getSelectUserCargo() {
        return SelectUserCargo;
    }

    public void setSelectUserCargo(String SelectUserCargo) {
        this.SelectUserCargo = SelectUserCargo;
    }

}
