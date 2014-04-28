/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package breadinterface;

import hpair.UnicodeDictionary;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

/**
 *
 * @author bkim11
 */
public class BIBar extends JPanel
{
    private BIButton _leftButton;
    private BIButton _rightButton;
    private BIButton _middleButton;
    
    public BIBar( String s )
    {
        super();
        
        _leftButton = new BIButton( (String) UnicodeDictionary.INFO );
        _rightButton = new BIButton( (String) UnicodeDictionary.MENU );
        _middleButton = new BIButton( s );
    }
    
    public void update()
    {
        this.removeAll();
        
        this.setLayout(new BorderLayout());
        
        this.add( _leftButton, BorderLayout.WEST );
        this.add( _middleButton, BorderLayout.CENTER );
        this.add( _rightButton, BorderLayout.EAST ); 
    }
    
    public void setup()
    {  
        this.setBackground( Color.BLACK );
        
        this.update();
    }
    
    
    public BIButton getLeftButton() { return _leftButton; }
    public void setLeftButton( String title ) { _leftButton = new BIButton( " "+title ); this.update(); }
    
    public BIButton getRightButton() { return _rightButton; }
    public void setRightButton( String title ) { _rightButton = new BIButton( title+" "); this.update(); }

    public BIButton getMiddleButton() { return _middleButton; }
    public void setMiddleButton( String title ) { _middleButton = new BIButton( title ); this.update(); }
    
    public void addRightButtonAction( ActionListener listener )
    { _rightButton.addActionListener(listener); }
    
    public void addLeftButtonAction( ActionListener listener )
    { _leftButton.addActionListener( listener ); }
    
    public void addMiddleButtonAction( ActionListener listener )
    { _middleButton.addActionListener( listener); }
}