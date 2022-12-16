/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modelos;



/**
 *
 * @author Sebastian
 */
public class HorarioModelo {
    
  private int idhorarios;
  private String horaInicio;
  private String horaFin;

    public HorarioModelo(int idhorarios, String horaInicio, String horaFin) {
        this.idhorarios = idhorarios;
        this.horaInicio = horaInicio;
        this.horaFin = horaFin;
    }

    public int getIdhorarios() {
        return idhorarios;
    }

    public void setIdhorarios(int idhorarios) {
        this.idhorarios = idhorarios;
    }

    public String getHoraInicio() {
        return horaInicio;
    }

    public void setHoraInicio(String horaInicio) {
        this.horaInicio = horaInicio;
    }

    public String getHoraFin() {
        return horaFin;
    }

    public void setHoraFin(String horaFin) {
        this.horaFin = horaFin;
    }
  
  
  
}
