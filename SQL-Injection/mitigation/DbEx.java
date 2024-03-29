// SQL imports
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DbEx {
    
    public void connectToAndQueryDatabase(String username, String password) {

        Connection con = DriverManagergetConnection(
                            "jdbc:myDriver:myDatabase",
                            username,
                            password);
        // createStatement, executeQuery
        Statement stmt = con.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT a, b, c FROM Table1");

        while (rs.next()) {
            int x = rs.getInt("a");
            String s = rs.getString("b");
            float f = rs.getFloat("c");
        }
        
        // PreparedStatement
        try {
            // Connection con = ...
            PreparedStatement pstmt = con.prepareStatement("SELECT * FROM users WHERE name= ?");
            pstmt.setString(1, "qqqqqq");
            pstmt.executeQuery();
        } catch (Exception e ) {
            System.out.println(e);
        }
    }

    public static void viewTable(Connection con, String dbName)
        throws SQLException {

        Statement stmt = null;
        String query = "select COF_NAME, SUP_ID, PRICE, " +
                    "SALES, TOTAL " +
                    "from " + dbName + ".COFFEES";
        try {
            stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next()) {
                String coffeeName = rs.getString("COF_NAME");
                int supplierID = rs.getInt("SUP_ID");
                float price = rs.getFloat("PRICE");
                int sales = rs.getInt("SALES");
                int total = rs.getInt("TOTAL");
                System.out.println(coffeeName + "\t" + supplierID +
                                "\t" + price + "\t" + sales +
                                "\t" + total);
            }
        } catch (SQLException e ) {
            JDBCTutorialUtilities.printSQLException(e);
        } finally {
            if (stmt != null) { stmt.close(); }
        }
    }
}