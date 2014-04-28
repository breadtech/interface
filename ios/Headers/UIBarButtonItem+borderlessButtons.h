//
//  UIBarButtonItem+borderlessButtons.h
//  breadgrader
//
//  Created by Brian Kim on 7/12/13.
//  Copyright (c) 2013 bread. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface UIBarButtonItem (borderlessButtons)
+ (UIBarButtonItem *)barItemWithImage:(UIImage *)image target:(id)target action:(SEL)action;
+ (UIBarButtonItem *)barButtonItemWithUnicode:(NSString *)u_string target:(id)target action:(SEL)action;
@end
