//
//  BIViewController.h
//  breadgrader
//
//  Created by Brian Kim on 7/27/13.
//  Copyright (c) 2013 breadtech. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "BIShareableItem.h"

@interface BIViewController : UIViewController

//
// convenience properties/methods
//

@property (nonatomic, weak) id<UIApplicationDelegate> appDelegate;
- (void)pop;
- (void)push:(UIViewController *)vc;

//
// BreadInterface Button Layout
//

// labels
@property (nonatomic, readonly) NSString *tl_label;
@property (nonatomic, readonly) NSString *tm_label; // the title
@property (nonatomic, readonly) NSString *tr_label;
@property (nonatomic, readonly) NSString *bl_label;
@property (nonatomic, readonly) NSString *bm_label;
@property (nonatomic, readonly) NSString *br_label;

// action
- (void)tl_clicked:(id)button;
- (void)tm_clicked:(id)button; // the help view
- (void)tr_clicked:(id)button;
- (void)bl_clicked:(id)button;
- (void)bm_clicked:(id)button;
- (void)br_clicked:(id)button;

// colors
@property (nonatomic, readonly) UIColor *fg;
@property (nonatomic, readonly) UIColor *bg;

//
// BreadInterface Lifecycle
//
- (id)init;
- (void)start;
- (void)resume;
- (void)update;
- (void)clear;
- (void)pause;
- (void)stop;
- (void)cleanup;

@end
