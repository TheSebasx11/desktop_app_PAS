/*
import com.digitalpersona.onetouch.DPFPDataPurpose;
import com.digitalpersona.onetouch.DPFPFeatureSet;
import com.digitalpersona.onetouch.DPFPGlobal;
import com.digitalpersona.onetouch.DPFPSample;
import com.digitalpersona.onetouch.DPFPTemplate;
import com.digitalpersona.onetouch.capture.DPFPCapture;
import com.digitalpersona.onetouch.capture.event.DPFPDataAdapter;
import com.digitalpersona.onetouch.capture.event.DPFPDataEvent;
import com.digitalpersona.onetouch.capture.event.DPFPErrorAdapter;
import com.digitalpersona.onetouch.capture.event.DPFPErrorEvent;
import com.digitalpersona.onetouch.capture.event.DPFPReaderStatusAdapter;
import com.digitalpersona.onetouch.capture.event.DPFPReaderStatusEvent;
import com.digitalpersona.onetouch.capture.event.DPFPSensorAdapter;
import com.digitalpersona.onetouch.capture.event.DPFPSensorEvent;
import com.digitalpersona.onetouch.processing.DPFPEnrollment;
import com.digitalpersona.onetouch.processing.DPFPFeatureExtraction;
import com.digitalpersona.onetouch.processing.DPFPImageQualityException;
import static com.digitalpersona.onetouch.processing.DPFPTemplateStatus.TEMPLATE_STATUS_FAILED;
import static com.digitalpersona.onetouch.processing.DPFPTemplateStatus.TEMPLATE_STATUS_READY;
import com.digitalpersona.onetouch.verification.DPFPVerification;
import com.digitalpersona.onetouch.verification.DPFPVerificationResult;*/
import conector.Operaciones;
import conector.conexion;
import java.util.ArrayList;
import java.util.Comparator;
import modelos.EmpleadoModel;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
/**
 *
 * @author Rusbel
 */
public class asignar_huella extends javax.swing.JFrame {

    /**
     * Creates new form asignar_huella
     */
    public conexion conect;
    public Operaciones ope;
    ArrayList<EmpleadoModel> ListaEmpleados = new ArrayList<>();

    /*private DPFPCapture Lector = DPFPGlobal.getCaptureFactory().createCapture();
    private DPFPEnrollment Reclutador = DPFPGlobal.getEnrollmentFactory().createEnrollment();
    private DPFPVerification Verificador = DPFPGlobal.getVerificationFactory().createVerification();
    private DPFPTemplate template;
    public static String TEMPLATE_PROPERTY = "template";
    public DPFPFeatureSet featuresInscripcion;
    public DPFPFeatureSet featuresVerificacion;*/
    public asignar_huella() {
        initComponents();
        conect = new conexion();
        ope = new Operaciones();
        llenarEmpleados();
    }

    public void llenarEmpleados() {

        try {
            ope.setSt(conect.getConexion().prepareStatement(ope.getSelectUserCargo()));
            ope.setRs(ope.getSt().executeQuery());
            while (ope.getRs().next()) {

                EmpleadoModel emp = new EmpleadoModel(ope.getRs().getInt("idusuarios"),
                        ope.getRs().getString("Nombre_Cargo"), ope.getRs().getInt("cargo"),
                        ope.getRs().getString("name_01"), ope.getRs().getString("name_02"),
                        ope.getRs().getString("lastname01"), ope.getRs().getString("lastname02"),
                        ope.getRs().getString("fecha_nac"),
                        ope.getRs().getString("identificacion"),
                        ope.getRs().getString("sexo"),
                        ope.getRs().getString("email"),
                        ope.getRs().getInt("telefono")
                );

                ListaEmpleados.add(emp);
            }
        } catch (Exception e) {
            System.out.println(e);
        }

        ListaEmpleados.sort(new Comparator<EmpleadoModel>() {
            @Override
            public int compare(EmpleadoModel o1, EmpleadoModel o2) {
                return o1.getName01().compareTo(o2.getName01());
            }
        });

        ListaEmpleados.forEach((e) -> {
            emp_menu.addItem("" + e.getFullName());
        });
    }

    /*
    public void guardarHuella() throws Exception {
        ByteArrayInputStream datosHuella = new ByteArrayInputStream(template.serialize());
        Integer tamHuella = template.serialize().length;
        
        String nombre = JOptionPane.showInputDialog("Nombre: ");
        
        try {
            conect.Conectar();
            var guardarStmt = (PreparedStatement) conect.getConexion().
                    prepareStatement("INSERT INTO huellas(usuarios_idusuarios, huehuella, huenombre) VALUES(?,?,?) ");
            
            guardarStmt.setInt(1, 1);
            guardarStmt.setBinaryStream(2, datosHuella, tamHuella);
            guardarStmt.setString(3, nombre);
            
            guardarStmt.execute();
            guardarStmt.close();
            JOptionPane.showMessageDialog(null, "Huella Guardada Correctamente");
            
            saveB.setEnabled(false);
            //verifyB.grabFocus();

        } catch (Exception e) {
            System.err.println(e);
        } finally {
            conect.Desconectar();
        }
    }
    
    public void verificarHuella(String nom) {
        try {
            conect.Conectar();
            
            java.sql.PreparedStatement verificarStmt
                    = conect.getConexion().prepareStatement("SELECT huehuella FROM huellas WHERE huenombre=?");
            verificarStmt.setString(1, nom);
            java.sql.ResultSet rs = verificarStmt.executeQuery();
            if (rs.next()) {
                byte templateBuffer[] = rs.getBytes("huehuella");
                
                DPFPTemplate referenceTemplate = DPFPGlobal.getTemplateFactory().createTemplate(templateBuffer);
                setTemplate(referenceTemplate);
                
                DPFPVerificationResult result = Verificador.verify(featuresVerificacion, getTemplate());
                
                if (result.isVerified()) {
                    JOptionPane.showMessageDialog(null, "La huella coincide con la de " + nom, " Verificacion de Huella", JOptionPane.OK_OPTION);
                } else {
                    JOptionPane.showMessageDialog(null, "No corresponde la hulla con " + nom, "Verificacion de huella", JOptionPane.ERROR_MESSAGE);
                }
            } else {
                JOptionPane.showMessageDialog(null, "No existe un registro de huella para " + nom, "Verificación de huella", JOptionPane.NO_OPTION);
            }
        } catch (Exception e) {
            System.err.println(e);
        } finally {
            conect.Desconectar();
        }
    }
    
    public void identificarHuella() throws Exception {
        try {
            conect.Conectar();
            java.sql.PreparedStatement identificarStmt = conect.getConexion().prepareStatement("SELECT * FROM huellas as H, usuarios as U WHERE H.usuarios_idusuarios = U.idusuarios;");//("SELECT huenombre, huehuella FROM huellas");

            java.sql.ResultSet rs = identificarStmt.executeQuery();
            
            while (rs.next()) {
                byte templateBuffer[] = rs.getBytes("huehuella");
                String nombre = rs.getString("name_01") + " " + rs.getString("lastname01")
                        + " " + rs.getString("lastname02"); //rs.getString("huenombre");

                DPFPTemplate referenceTemplate = DPFPGlobal.getTemplateFactory().createTemplate(templateBuffer);
                
                setTemplate(referenceTemplate);
                
                DPFPVerificationResult result = Verificador.verify(featuresVerificacion, getTemplate());
                
                if (result.isVerified()) {
                    idHuella = rs.getInt("idhuellas");
                    EnviarTexto("Las huellas capturada es de " + nombre);
                    JOptionPane.showMessageDialog(null, "Las huellas capturada es de " + nombre, "Verificación de huella", JOptionPane.INFORMATION_MESSAGE);
                    
                    return;
                }
            }
            JOptionPane.showMessageDialog(null, "No existe ningún registro que coincide con la huella", "Verificación de huella", JOptionPane.ERROR_MESSAGE);
            
            setTemplate(null);
            
        } catch (Exception e) {
            System.err.println("Error al identificar huella dactilar." + e.getMessage());
        } finally {
            conect.Desconectar();
        }
    }
    
    public DPFPFeatureSet extraerCaracteristicas(DPFPSample sample, DPFPDataPurpose purpose) {
        
        DPFPFeatureExtraction extractor = DPFPGlobal.getFeatureExtractionFactory().createFeatureExtraction();
        
        try {
            return extractor.createFeatureSet(sample, purpose);
        } catch (DPFPImageQualityException e) {
            return null;
        }
    }
    
    public Image CrearImagenHuella(DPFPSample sample) {
        return DPFPGlobal.getSampleConversionFactory().createImage(sample);
    }
    
    public void DibujarHuella(Image image) {
        lbImage.setIcon(new ImageIcon(image.getScaledInstance(lbImage.getWidth(), lbImage.getHeight(), Image.SCALE_DEFAULT)));
        repaint();
    }
    
    public void EstadoHuellas() {
        EnviarTexto("Muestra de huellas necesarias para guardar template " + Reclutador.getFeaturesNeeded());
    }
    
    public void start() {
        Lector.startCapture();
        EnviarTexto("Utilizando el Lector de Huella Dactilar");
    }
    
    public void stop() {
        Lector.stopCapture();
        EnviarTexto("No se está usando el Lector de Huella Dactilar");
    }
    
    public DPFPTemplate getTemplate() {
        return template;
    }
    
    public void setTemplate(DPFPTemplate temp) {
        DPFPTemplate old = this.template;
        this.template = temp;
        firePropertyChange(TEMPLATE_PROPERTY, old, temp);
    }
    
    public void ProcesarCaptura(DPFPSample sample) {
        featuresInscripcion = extraerCaracteristicas(sample, DPFPDataPurpose.DATA_PURPOSE_ENROLLMENT);
        
        featuresVerificacion = extraerCaracteristicas(sample, DPFPDataPurpose.DATA_PURPOSE_VERIFICATION);
        
        if (featuresInscripcion != null) {
            try {
                System.out.println("Las caracteristicas de la Huella ha sido creada");
                Reclutador.addFeatures(featuresInscripcion);
                
                Image image = CrearImagenHuella(sample);
                DibujarHuella(image);
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
            } finally {
                EstadoHuellas();
                switch (Reclutador.getTemplateStatus()) {
                    case TEMPLATE_STATUS_READY:
                        stop();
                        setTemplate(Reclutador.getTemplate());
                        EnviarTexto("La plantilla de la huella ha sido creada");
                        HuellaCaptured = true;
                        if (HuellaCaptured && fotoCaptured) {
                            saveB.setEnabled(true);
                        }
                        try {
                            identificarHuella();
                            Reclutador.clear();
                        } catch (Exception e) {
                            System.err.println(e);
                        }
                        break;
                    case TEMPLATE_STATUS_FAILED:
                        Reclutador.clear();
                        stop();
                        EstadoHuellas();
                        setTemplate(null);
                        JOptionPane.showMessageDialog(asistenciahuella.this, "Algo salió mal");
                    default:
                    
                }
            }
        }
    }
    
    protected void Iniciar() {
        Lector.addDataListener(new DPFPDataAdapter() {
            @Override
            public void dataAcquired(final DPFPDataEvent e) {
                SwingUtilities.invokeLater(new Runnable() {
                    @Override
                    public void run() {
                        EnviarTexto("La huella ha sido Capturada");
                        ProcesarCaptura(e.getSample());
                    }
                });
            }
        });
        
        Lector.addReaderStatusListener(new DPFPReaderStatusAdapter() {
            @Override
            public void readerConnected(final DPFPReaderStatusEvent e) {
                SwingUtilities.invokeLater(new Runnable() {
                    @Override
                    public void run() {
                        EnviarTexto("El Sensor de Huella Digital está Activado o conectado");
                    }
                });
            }
            
            @Override
            public void readerDisconnected(DPFPReaderStatusEvent e) {
                SwingUtilities.invokeLater(new Runnable() {
                    @Override
                    public void run() {
                        EnviarTexto("El Sensor de Huella Digital está desactivado o no Conectado");
                    }
                });
            }
        });
        
        Lector.addSensorListener(new DPFPSensorAdapter() {
            @Override
            public void fingerTouched(DPFPSensorEvent dpfpse) {
                SwingUtilities.invokeLater(new Runnable() {
                    @Override
                    public void run() {
                        EnviarTexto("Dedo colocado ");
                    }
                });
            }
            
            @Override
            public void fingerGone(DPFPSensorEvent dpfpse) {
                SwingUtilities.invokeLater(new Runnable() {
                    @Override
                    public void run() {
                        EnviarTexto("Dedo quitado ");
                    }
                });
            }
            
            @Override
            public void imageAcquired(DPFPSensorEvent dpfpse) {
                
            }
        });
        Lector.addErrorListener(new DPFPErrorAdapter() {
            public void errorOccured(DPFPErrorEvent e) {
                SwingUtilities.invokeLater(new Runnable() {
                    @Override
                    public void run() {
                        EnviarTexto("Error: " + e.getError());
                    }
                });
            }
        });
    }
     
    private void closeAll() {
        webcam.close();
        webcamPanel.stop();
    }

    private void sendData(int id, File image) {
        FileInputStream fis = null;
        try {
            ope.setSt(con.getConexion().prepareStatement("Call r_salida(?,?)"));
            //InputStream resourceBuff = this.getClass().getResourceAsStream(image.getAbsolutePath());

            fis = new FileInputStream(image);
            byte b[] = new byte[(int) image.length()];
            fis.read(b);
            java.sql.Blob b2 = new SerialBlob(b);

            ope.getSt().setInt(1, id);
            ope.getSt().setBlob(2, b2);

            ope.setRs(ope.getSt().executeQuery());

            while (ope.getRs().next()) {
                JOptionPane.showMessageDialog(null, ope.getRs().getString("msg"));
            }
            JOptionPane.showMessageDialog(null, "Agregado con exito");
        } catch (Exception e) {
            System.out.println(e);
        }

    }*/
    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel2 = new javax.swing.JPanel();
        jPanel4 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        emp_menu = new javax.swing.JComboBox<>();
        lbImage = new javax.swing.JLabel();
        lbImage1 = new javax.swing.JLabel();
        jButton1 = new javax.swing.JButton();
        jButton3 = new javax.swing.JButton();
        jButton2 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jLabel1.setBackground(new java.awt.Color(0, 0, 0));
        jLabel1.setFont(new java.awt.Font("Comic Sans MS", 0, 18)); // NOI18N
        jLabel1.setText("Asignar huella");

        jLabel4.setFont(new java.awt.Font("Comic Sans MS", 0, 14)); // NOI18N
        jLabel4.setText("Empleado");

        javax.swing.GroupLayout jPanel4Layout = new javax.swing.GroupLayout(jPanel4);
        jPanel4.setLayout(jPanel4Layout);
        jPanel4Layout.setHorizontalGroup(
            jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel4Layout.createSequentialGroup()
                .addGap(288, 288, 288)
                .addComponent(jLabel1)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
            .addGroup(jPanel4Layout.createSequentialGroup()
                .addContainerGap(143, Short.MAX_VALUE)
                .addComponent(jLabel4, javax.swing.GroupLayout.PREFERRED_SIZE, 116, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(57, 57, 57)
                .addComponent(emp_menu, javax.swing.GroupLayout.PREFERRED_SIZE, 315, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(92, 92, 92))
        );
        jPanel4Layout.setVerticalGroup(
            jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel4Layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jLabel1)
                .addGap(29, 29, 29)
                .addGroup(jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(emp_menu, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel4))
                .addGap(212, 212, 212))
        );

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addComponent(jPanel4, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 0, Short.MAX_VALUE))
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel4, javax.swing.GroupLayout.PREFERRED_SIZE, 112, javax.swing.GroupLayout.PREFERRED_SIZE)
        );

        lbImage.setText("Huella");
        lbImage.setVerticalAlignment(javax.swing.SwingConstants.TOP);

        lbImage1.setText("Huella");
        lbImage1.setVerticalAlignment(javax.swing.SwingConstants.TOP);

        jButton1.setText("Capturar informacion");

        jButton3.setText("Salir");
        jButton3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton3ActionPerformed(evt);
            }
        });

        jButton2.setText("Asignar informacion");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 1, Short.MAX_VALUE))
            .addGroup(layout.createSequentialGroup()
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(lbImage, javax.swing.GroupLayout.PREFERRED_SIZE, 302, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(lbImage1, javax.swing.GroupLayout.PREFERRED_SIZE, 334, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jButton1)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(130, 130, 130)
                                .addComponent(jButton2)))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(jButton3, javax.swing.GroupLayout.PREFERRED_SIZE, 165, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(139, 139, 139))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(6, 6, 6)
                .addComponent(jButton1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lbImage1, javax.swing.GroupLayout.PREFERRED_SIZE, 264, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lbImage, javax.swing.GroupLayout.PREFERRED_SIZE, 265, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 25, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jButton2)
                    .addComponent(jButton3))
                .addGap(21, 21, 21))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButton3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton3ActionPerformed
        ventana01 principal = new ventana01();
        principal.setVisible(true);
        this.dispose();        // TODO add your handling code here:
    }//GEN-LAST:event_jButton3ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Windows".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(asignar_huella.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(asignar_huella.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(asignar_huella.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(asignar_huella.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new asignar_huella().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JComboBox<String> emp_menu;
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JButton jButton3;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JPanel jPanel4;
    private javax.swing.JLabel lbImage;
    private javax.swing.JLabel lbImage1;
    // End of variables declaration//GEN-END:variables
}
