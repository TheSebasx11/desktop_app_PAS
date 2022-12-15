/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modelos;

import java.util.Date;

/**
 *
 * @author Sebastian
 */
public class EmpleadoModel {

    private int idusuarios;
    private String cargo;
    // ignore: non_constant_identifier_names
    private int id_cargo;
    private String name01;
    private String name02;
    private String lastname01;
    private String lastname02;
    private String fechaNac;

    private String identificacion;
    private String sexo;
    private String email;
    private int telefono;

    public EmpleadoModel(int idusuarios, String cargo, int id_cargo, String name01, String name02, String lastname01, String lastname02, String fechaNac, String identificacion, String sexo, String email, int telefono) {
        this.idusuarios = idusuarios;
        this.cargo = cargo;
        this.id_cargo = id_cargo;
        this.name01 = name01;
        this.name02 = name02;
        this.lastname01 = lastname01;
        this.lastname02 = lastname02;
        this.fechaNac = fechaNac;
        this.identificacion = identificacion;
        this.sexo = sexo;
        this.email = email;
        this.telefono = telefono;
    }

    public int getIdusuarios() {
        return idusuarios;
    }

    public void setIdusuarios(int idusuarios) {
        this.idusuarios = idusuarios;
    }

    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public int getId_cargo() {
        return id_cargo;
    }

    public void setId_cargo(int id_cargo) {
        this.id_cargo = id_cargo;
    }

    public String getName01() {
        return name01;
    }

    public void setName01(String name01) {
        this.name01 = name01;
    }

    public String getName02() {
        return name02;
    }

    public void setName02(String name02) {
        this.name02 = name02;
    }

    public String getLastname01() {
        return lastname01;
    }

    public void setLastname01(String lastname01) {
        this.lastname01 = lastname01;
    }

    public String getLastname02() {
        return lastname02;
    }

    public void setLastname02(String lastname02) {
        this.lastname02 = lastname02;
    }

    public String getFechaNac() {
        return fechaNac;
    }

    public void setFechaNac(String fechaNac) {
        this.fechaNac = fechaNac;
    }

    public String getIdentificacion() {
        return identificacion;
    }

    public void setIdentificacion(String identificacion) {
        this.identificacion = identificacion;
    }

    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

}
