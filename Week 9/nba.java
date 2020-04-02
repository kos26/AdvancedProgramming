import java.sql.*;

public class nba {

  public static void main( String args[] ) {

   Connection c = null;
   Statement stmt = null;
   try {
      //Class.forName("org.sqlite.JDBC");
      c = DriverManager.getConnection("jdbc:sqlite:nba.db");
      c.setAutoCommit(false);
      System.out.printf("\n\nOpened database successfully\n\n");
      System.out.printf("\n\nNames of all the players who played for Philadelphia 76ers during season 2017-18:\n\n");

      stmt = c.createStatement();
      ResultSet rs = stmt.executeQuery( "SELECT player FROM nba where team = 'Philadelphia 76ers' and season = '2017-18'");
      
      while ( rs.next() ) {
         String  player = rs.getString("player");
         
         System.out.println( player );
         System.out.println();
      }
      rs.close();

      System.out.printf("**************************************************************************");

      System.out.printf("\n\nNames of all the distinct teams Allen Iverson played for:\n\n");

      ResultSet s = stmt.executeQuery( "SELECT DISTINCT team FROM nba where player = 'Allen Iverson'");
      
      while ( s.next() ) {
         String  team = s.getString("team");
         System.out.println( team );
         System.out.println();
      }
      s.close();
      stmt.close();
      c.close();
   } catch ( Exception e ) {
      System.err.println( e.getClass().getName() + ": " + e.getMessage() );
      System.exit(0);
   }
   System.out.println("\n\nQueries completed successfully!!");
  }
}
