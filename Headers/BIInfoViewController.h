//
//  BIInfoViewController.h
//  breadgrader
//
//  Created by Brian Kim on 3/24/13.
//  Copyright (c) 2013 bread. All rights reserved.
//

/*********************/

#import <UIKit/UIKit.h>
#import "BITableViewController.h"

@class BIInfoCell;
@class BIInfoLayout;
@class BIInfoViewController;

@protocol BIInfoViewControllerDelegate
- (void)infoViewController:(BIInfoViewController *)vc didSaveWithInfo:(NSDictionary *)info;
@end

@interface BIInfoViewController : BITableViewController <UITextFieldDelegate, UITextViewDelegate>

@property (nonatomic, weak) id<BIInfoViewControllerDelegate> delegate;

// define a custom info layout class to define the layout of your vc
@property (nonatomic, strong) BIInfoLayout *infoLayout;

// convenience accessor methods

// date picker stuff
- (void)toggleDatePicker:(UIDatePicker *)datePicker turnOn:(BOOL)on;

+ (UIDatePicker *)aDatePicker:(CGFloat)width target:(id)target action:(SEL)action;

// override = true
- (void)wantsToPickValueForCellAtIndexPath:(NSIndexPath *)ip;

@end
