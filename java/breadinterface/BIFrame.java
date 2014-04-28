//
// title = BIFrame.java
// by = Brian Kim
// description = 
//

package breadinterface;

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.event.*;
import javax.swing.*;

/**
 *
 * @author bkim11
 */
public abstract class BIFrame extends JFrame
{
    // view
    private String _title;
    private BIBar _topBar;
    private BIBar _bottomBar;
    private JPanel _mainView;
    
    public BIFrame( String s )
    {
        super( s );
        
        _title = s;
        
        this.init();
    }
    
    public void start() { this.setVisible( true ); }
    
    public JPanel getMainView() { return _mainView; }
    
    public BIButton getTl() { return _topBar.getLeftButton(); }
    public void setTl( String text ) { _topBar.setLeftButton(text); }
    public void setTlAction( ActionListener a ) { _topBar.addLeftButtonAction( a ); }
        
    public BIButton getTr() { return _topBar.getRightButton(); }
    public void setTr( String text ) { _topBar.setRightButton(text); }
    public void setTrAction( ActionListener a ) { _topBar.addRightButtonAction( a ); }
    
    public BIButton getTm() { return _topBar.getMiddleButton(); }
    public void setTm( String text ) { _topBar.setMiddleButton(text); }
    public void setTmAction( ActionListener a ) { _topBar.addMiddleButtonAction( a ); }
    
    public BIButton getBl() { return _bottomBar.getLeftButton(); }
    public void setBl( String text ) { _bottomBar.setLeftButton( text ); }
    public void setBlAction( ActionListener a ) { _bottomBar.addLeftButtonAction( a ); }
    
    public BIButton getBr() { return _bottomBar.getRightButton(); }
    public void setBr( String text ) { _bottomBar.setRightButton( text ); }
    public void setBrAction( ActionListener a ) { _bottomBar.addRightButtonAction( a ); }
    
    public BIButton getBm() { return _bottomBar.getMiddleButton(); }
    public void setBm( String text) { _bottomBar.setMiddleButton( text ); }
    public void setBmAction( ActionListener a ) { _bottomBar.addMiddleButtonAction( a ); }
    
    
    
    public void setup()
    {
        this.setSize( 960, 640 );       
        
        _topBar = new BIBar( _title );
        _bottomBar = new BIBar( "b" );
        _mainView = new JPanel();
        
        _topBar.setup();
        _bottomBar.setup();
        
        Container c = getContentPane();
        c.add( _mainView, BorderLayout.CENTER );
        c.add( _topBar, BorderLayout.NORTH );
        c.add( _bottomBar, BorderLayout.SOUTH );
    }
    
    public void update()
    {
        _topBar.update();
        _bottomBar.update();
    }
    
    protected void init()
    {
        this.setup();
        
        this.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );
    }
    
}
