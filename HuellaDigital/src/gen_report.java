
import com.mysql.jdbc.ResultSetMetaData;
import conector.Operaciones;
import conector.conexion;
import javax.swing.table.DefaultTableModel;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
/**
 *
 * @author Jose Perez
 */
public class gen_report extends javax.swing.JFrame {

    /**
     * Creates new form gen_report
     */
    public conexion con;
    public Operaciones ope;
    private DefaultTableModel DTM;

    String numAsistencia = "SELECT COUNT(turnos.llegada) as Asistencia, usuarios.* FROM turnos, usuarios  INNER JOIN usuarios_has_horarios AS U ON U.usuarios_idusuarios = usuarios.idusuarios  WHERE turnos.usuarios_idusuarios = usuarios.idusuarios GROUP BY usuarios.idusuarios;";
    String numInasistencia = "SELECT COUNT(U.idusuarios) as Inasistencia, U.* FROM usuarios as U WHERE U.idusuarios NOT IN (SELECT usuarios.idusuarios from usuarios INNER JOIN turnos as T ON T.usuarios_idusuarios = usuarios.idusuarios WHERE T.llegada IS NOT NULL) GROUP BY U.idusuarios;";
    String puntuales = "SELECT DISTINCT usuarios.*, h.hora_inicio, T.llegada FROM usuarios  INNER JOIN turnos as T ON T.usuarios_idusuarios = usuarios.idusuarios INNER JOIN usuarios_has_horarios as UH ON UH.usuarios_idusuarios = usuarios.idusuarios inner join horarios as h on h.idhorarios = UH.horarios_idhorarios WHERE T.llegada <= h.hora_inicio";
    String impuntuales = "SELECT usuarios.*, h.hora_inicio, T.llegada FROM usuarios  INNER JOIN turnos as T ON T.usuarios_idusuarios = usuarios.idusuarios INNER JOIN usuarios_has_horarios as UH ON UH.usuarios_idusuarios = usuarios.idusuarios inner join horarios as h on h.idhorarios = UH.horarios_idhorarios WHERE T.llegada > h.hora_inicio;";

    public gen_report() {
        initComponents();
        con = new conexion();
        ope = new Operaciones();
        DTM = (DefaultTableModel) table.getModel();

    }

    public void MostrarReporte() {

        DTM.setColumnCount(0);
        DTM.setRowCount(0);
//        System.out.println(menu.getSelectedIndex() + "");
        try {
            /*  Empleados mas puntuales
                Empleados mas impuntuales
                Empleados faltantes
                Asistencia*/
            DTM.addColumn("Nombre 1");
            DTM.addColumn("Nombre 2");
            DTM.addColumn("Apellido 1");
            DTM.addColumn("Apellido 2");
            DTM.addColumn("Nacimiento");
            DTM.addColumn("Identificación");
            DTM.addColumn("Sexo");
            DTM.addColumn("Email");
            switch (menu.getSelectedIndex()) {
                case 0:
                    ope.setSt(con.getConexion().prepareStatement(puntuales));

                    DTM.addColumn("Hora Inicio");
                    DTM.addColumn("Llegada");
                    break;
                case 1:
                    ope.setSt(con.getConexion().prepareStatement(impuntuales));
                    DTM.addColumn("Hora Inicio");
                    DTM.addColumn("Llegada");

                    break;
                case 2:
                    ope.setSt(con.getConexion().prepareStatement(numInasistencia));
                    DTM.addColumn("Inasistencia");

                    break;
                case 3:
                    ope.setSt(con.getConexion().prepareStatement(numAsistencia));
                    DTM.addColumn("Asistencia");
                    break;
                default:

            }

            ope.setRs(ope.getSt().executeQuery());
            ResultSetMetaData rsmd = (ResultSetMetaData) ope.getRs().getMetaData();

            /*  for (int i = 0; i < rsmd.getColumnCount() - 4; i++) {
                System.out.println("" + i + "" + rsmd.getColumnName(0) );
//                DTM.addColumn(rsmd.getColumnLabel(i));
            }*/
            //System.out.println("" + rsmd.getColumnLabel(0) );
            //System.out.println("" + rsmd.getColumnClassName(0));
            while (ope.getRs().next()) {

                int fila = DTM.getRowCount();
                DTM.setRowCount(fila + 1);
                /*    for (int i = 0; i < rsmd.getColumnCount(); i++) {
                    DTM.setValueAt(ope.getRs().getString(rsmd.getColumnName(i)), fila, i);
                }*/

                DTM.setValueAt(ope.getRs().getString("name_01"), fila, 0);
                DTM.setValueAt(ope.getRs().getString("name_02"), fila, 1);
                DTM.setValueAt(ope.getRs().getString("lastname01"), fila, 2);
                DTM.setValueAt(ope.getRs().getString("lastname02"), fila, 3);
                DTM.setValueAt(ope.getRs().getString("fecha_nac"), fila, 4);
                DTM.setValueAt(ope.getRs().getString("identificacion"), fila, 5);
                DTM.setValueAt(ope.getRs().getString("sexo"), fila, 6);
                DTM.setValueAt(ope.getRs().getString("email"), fila, 7);

                switch (menu.getSelectedIndex()) {
                    case 0:
                        ope.setSt(con.getConexion().prepareStatement(puntuales));
                        DTM.setValueAt(ope.getRs().getString("hora_inicio"), fila, 8);
                        DTM.setValueAt(ope.getRs().getString("llegada"), fila, 9);

                        break;
                    case 1:
                        ope.setSt(con.getConexion().prepareStatement(impuntuales));
                        DTM.setValueAt(ope.getRs().getString("hora_inicio"), fila, 8);
                        DTM.setValueAt(ope.getRs().getString("llegada"), fila, 9);

                        break;
                    case 2:
                        ope.setSt(con.getConexion().prepareStatement(numInasistencia));
                        DTM.setValueAt(ope.getRs().getString("Inasistencia"), fila, 8);

                        break;
                    case 3:
                        ope.setSt(con.getConexion().prepareStatement(numAsistencia));
                        DTM.setValueAt(ope.getRs().getString("Asistencia"), fila, 8);
                        break;
                    default:

                }

                /*    DTM.setValueAt(quer.getRs().getString("Nombres"), fila, 0);
                DTM.setValueAt(quer.getRs().getString("Apellidos"), fila, 1);
                DTM.setValueAt(quer.getRs().getString("Identificacion"), fila, 2);
                DTM.setValueAt(quer.getRs().getString("Fecha"), fila, 3);
                DTM.setValueAt(quer.getRs().getString("Llegada"), fila, 4);
                DTM.setValueAt(quer.getRs().getString("Salida"), fila, 5);*/
            }

        } catch (Exception e) {
            System.out.println(e);
        }

    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        jButton1 = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        table = new javax.swing.JTable();
        jButton2 = new javax.swing.JButton();
        menu = new javax.swing.JComboBox<>();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setResizable(false);

        jPanel1.setBackground(new java.awt.Color(204, 0, 0));

        jLabel1.setFont(new java.awt.Font("Comic Sans MS", 0, 18)); // NOI18N
        jLabel1.setForeground(new java.awt.Color(255, 255, 255));
        jLabel1.setText("Reporte de empleados");

        jButton1.setFont(new java.awt.Font("Comic Sans MS", 0, 14)); // NOI18N
        jButton1.setText("Generar");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        table.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {

            },
            new String [] {

            }
        ));
        jScrollPane1.setViewportView(table);

        jButton2.setFont(new java.awt.Font("Comic Sans MS", 0, 14)); // NOI18N
        jButton2.setText("Volver");
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });

        menu.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Empleados mas puntuales", "Empleados mas impuntuales", "Empleados faltantes", "Asistencia" }));
        menu.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                menuActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(37, 37, 37)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(jLabel1)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 59, Short.MAX_VALUE)
                        .addComponent(menu, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(107, 107, 107)
                        .addComponent(jButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 157, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jButton2))
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 764, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(9, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(44, 44, 44)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel1)
                    .addComponent(jButton1)
                    .addComponent(jButton2)
                    .addComponent(menu, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 23, Short.MAX_VALUE)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 400, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        pack();
        setLocationRelativeTo(null);
    }// </editor-fold>//GEN-END:initComponents

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        adminprincpial01 ap = new adminprincpial01();
        ap.setVisible(true);
        this.dispose();
    }//GEN-LAST:event_jButton2ActionPerformed

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        // TODO add your handling code here:
        MostrarReporte();
    }//GEN-LAST:event_jButton1ActionPerformed

    private void menuActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_menuActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_menuActionPerformed

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
            java.util.logging.Logger.getLogger(gen_report.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(gen_report.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(gen_report.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(gen_report.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new gen_report().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JComboBox<String> menu;
    private javax.swing.JTable table;
    // End of variables declaration//GEN-END:variables
}
