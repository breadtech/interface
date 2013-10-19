//
//  UIBarButtonItem+borderlessButtons.m
//  breadgrader
//
//  Created by Brian Kim on 7/12/13.
//  Copyright (c) 2013 bread. All rights reserved.
//

#import "UIBarButtonItem+borderlessButtons.h"

@implementation UIBarButtonItem (borderlessButtons)

+ (UIBarButtonItem *)barItemWithImage:(UIImage *)image target:(id)target action:(SEL)action
{
    UIImageView *iview = [[UIImageView alloc] initWithImage: image];
    iview.frame = CGRectMake( 5.0,  5.0,  20.0, 20.0);
    
    UIButton *button = [UIButton buttonWithType: UIButtonTypeCustom];

    [button setFrame: CGRectMake( 0.0, 0.0, 30.0, 30.0)];
    [button addSubview: iview];
    [button addTarget: target action: action forControlEvents: UIControlEventTouchUpInside];
    [button setImage: image forState: UIControlStateNormal];
    [button setShowsTouchWhenHighlighted: YES];
    
    UIBarButtonItem *b = [[UIBarButtonItem alloc] initWithCustomView: button];
    b.image = image;
    return b;
}

@end
