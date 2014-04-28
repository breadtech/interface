/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package breadinterface;

import java.awt.Color;
import java.awt.Font;
import javax.swing.*;
import java.awt.Graphics;

/**
 *
 * @author bkim11
 */
public class BIButton extends JButton 
{
    private Color hoverBackgroundColor = Color.lightGray;
    private Color pressedBackgroundColor = Color.lightGray.brighter().brighter(); 
    
    public Color getHoverBackgroundColor() {
        return hoverBackgroundColor;
    }

    public void setHoverBackgroundColor(Color hoverBackgroundColor) {
        this.hoverBackgroundColor = hoverBackgroundColor;
    }

    public Color getPressedBackgroundColor() {
        return pressedBackgroundColor;
    }

    public void setPressedBackgroundColor(Color pressedBackgroundColor) {
        this.pressedBackgroundColor = pressedBackgroundColor;
    }
    
    public BIButton()
    {
        super();
    }
    
    public BIButton( String s )
    {
        super( s );
        
        super.setFont( new Font( Font.SANS_SERIF , Font.PLAIN, 30 ) );
        super.setForeground(Color.white);
        super.setBorder( null );
    }
}
