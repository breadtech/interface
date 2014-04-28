//
//  BIColorAlertView.h
//  breadgrader
//
//  Created by Brian Kim on 3/6/13.
//  Copyright (c) 2013 bread. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface BIColorAlertView : UIView
@property (nonatomic) float scale; // rate the situation from 0 to 10; 0 = worst; 10 = best
+ (UIColor *)colorForScale:(float)scale;
@end
