//
//  BIInfoViewController.m
//  breadgrader
//
//  Created by Brian Kim on 3/24/13.
//  Copyright (c) 2013 bread. All rights reserved.
//

#import "BIInfoCell.h"
#import "BIInfoLayout.h"
#import "BIInfoViewController.h"

@interface BIInfoViewController ()
@end

@implementation BIInfoViewController

#pragma mark - accessor methods

- (BIInfoLayout *)infoLayout
{
    if (!_infoLayout)
    {
        _infoLayout = [BIInfoLayout defaultLayout];
    }
    return _infoLayout;
}

- (BOOL)wantsGroupedStyle
{
    return YES;
}

#define DATEPICKER_HEIGHT 280.0f

+ (UIDatePicker *)aDatePicker:(CGFloat)width target:(id)target action:(SEL)action
{
    UIDatePicker *datePicker;
    CGRect rect = CGRectZero;
    
    rect.size = CGSizeMake( width, DATEPICKER_HEIGHT);

    datePicker = [[UIDatePicker alloc] initWithFrame: rect];
    datePicker.date = [NSDate date];
    datePicker.datePickerMode = UIDatePickerModeDateAndTime;
        
    [datePicker addTarget: target action: action forControlEvents: UIControlEventValueChanged];
    datePicker.autoresizingMask = UIViewAutoresizingFlexibleWidth;
    
    return datePicker;
}

#pragma mark - convenience methods

#define ANIMATION_SPEED 0.25f

- (void)toggleDatePicker:(UIDatePicker *)datePicker turnOn:(BOOL)on
{
    [UIView animateWithDuration: ANIMATION_SPEED
                     animations: ^
     {
         self.navigationController.toolbarHidden = NO;
         CGRect datePickerFrame = datePicker.frame;
         datePickerFrame.origin.y = self.view.window.frame.size.height;
         
         datePicker.frame = datePickerFrame;
     }
                     completion:^(BOOL finished)
     {
         if (on)
         {
             
         }
         else
         {
             [datePicker removeFromSuperview];
         }
     }];
}

#pragma mark - Public API

- (void)setupUI
{
    /*
    self.tl = self.noButton;
    self.br = self.closeButton;
    self.tr = self.doneButton;
    
    self.tableView.dataSource = self.infoLayout;
    
    [super setupUI];
     */
}

- (void)doneButtonPressed:(id)sender
{
}

- (void)wantsToPickValueForCellAtIndexPath:(NSIndexPath *)ip
{
    // abstract
}

#pragma mark - UITableViewDelegate

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    BIInfoCell *cell = (BIInfoCell *)[self.tableView cellForRowAtIndexPath: indexPath];
    if (cell.type == InfoTypePicker)
        [self wantsToPickValueForCellAtIndexPath: indexPath];
    else if (cell.type == InfoTypeFill)
    {
        [cell.textField1 becomeFirstResponder];
    }
    else if (cell.type == InfoTypeFill2)
    {
        if (cell.textField1.isFirstResponder && cell.textField2)
        {
            [cell.textField2 becomeFirstResponder];
        } else
        {
            [cell. textField1 becomeFirstResponder];
        }
    }
    else if (cell.type == InfoTypeTextView)
    {
        [cell.textView becomeFirstResponder];
    }
    
    [self.tableView deselectRowAtIndexPath: indexPath animated: YES];
}

#pragma mark - Keyboard management

- (BOOL)textFieldShouldReturn:(UITextField *)textField
{
    [textField resignFirstResponder];
    return YES;
}

@end
