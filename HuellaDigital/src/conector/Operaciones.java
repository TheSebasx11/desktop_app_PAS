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

    public Operaciones() {
        st = null;
        rs = null;
        SelectUserCargo = "SELECT usuarios.*, cargos.nombre as Nombre_Cargo FROM `usuarios`, cargos WHERE usuarios.cargo = cargos.id_cargo";
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
