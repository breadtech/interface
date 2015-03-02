Introduction

BreadInterface (BI) is a user-interface standard that reveals the simplicity of software.
It will help developers create apps more easily and for the average person 
 to use it more efficiently.
As the reader, you are given the mission of learning to be a user of BI. 
Additionally, you can venture to the more technically oriented task of 
 learning how to make apps (both mobile and desktop) that leverage BI. 

Basics: The Button

The core philosophy of BreadInterface is the importance of a Button. 
Buttons have a label and perform an action when clicked. 
The definition of the content and functionality of all buttons 
 is decided by the programmer. 
Another fundamental philosophy of BreadInterface is that learning how 
 write apps is a relatively easy task for any individual who is 
 willing to commit his/her time and effort (min. 1 hr/day) in the craft.


The Menu:

However, whether you are a user or developer, we hope you can appreciate 
 the power of BreadInterface in the templated layout of the Buttons in a BI Menu
The BI Menu contains up to six buttons arranged in a manner that will become 
 increasingly familiar as more BI apps are used and developed.
These buttons are generically named as follows:

                      |------------------|
 - top-left      (tl) | tl     tm     tr |
                      |------------------|
 - top-middle    (tm) |  BreadInterface  |
                      |   by BreadTech   |
 - top-right     (tr) |                  |
                      |                  |
 - bottom-left   (bl) |   How Bread is   |
                      |    Your App?     |
 - bottom-middle (bm) |                  |
                      |------------------|
 - bottom-right  (br) | bl     bm     br |
                      |------------------|

User Checkpoint:

At this juncture of the manual, we believe that the magic of BreadInterface can best be 
 experienced through a demo.
The first BI app ever developed is our first product, BreadGrader (http://www.BreadTech.com/Grader) 
Hopefully, the elements of BI should stand-out clearly whether you are a technology user or developer.

We are hoping to release an updated iOS app as well as add support for Android and PC by the end of Spring 2015.
Despite the outdated-ness of BreadGrader (BG), we hope that 

Up Ahead...
From here onward will be a step-by-step guide on how to develop BreadGrader (ultimately learning how to use BI)
using the Python programming language.

For Developers (or Brave Users)

More On Buttons:

Looking at the figure above, instead of initials, one should expect one single character  
 that accurately describes the functionality of a button.
For buttons, instead of characters, we would like to call them glyphs.
For example, activing some add functionality is commonly expressed with a 
 button containing the '+' glyph.
Technology has matured to a point where up to 65535 possible glyphs can be expressed simply as numbers,
 called Unicode, or more popularly referred to as Emoji.
However, different platforms (like iOS, Android, and Windows) and versions have 
 varying limitations in the rendering (or drawing) of all these glyphs.
The ultimate goal of BI is to be able to develop purely platform independent code,
 but until all the popular platforms can fully support the Unicode character set.



The center portion of the Frame is a View who's content is ultimately decided by the programmer.
functionality. Common examples include a list view, info view, or even another frame as a submenu.

To get started, check out the Samples.py script inside the BreadInterface module
