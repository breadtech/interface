//
//  BIColorAlertView.m
//  breadgrader
//
//  Created by Brian Kim on 3/6/13.
//  Copyright (c) 2013 bread. All rights reserved.
//

#import "BIColorAlertView.h"


@implementation BIColorAlertView

- (void)setScale:(float)scale
{
    _scale = scale;
    [self setNeedsDisplay];
}

- (void)setup
{
    self.contentMode = UIViewContentModeRedraw;
    self.backgroundColor = [UIColor clearColor];
}

- (void)awakeFromNib
{
    [self setup]; // get initialized when we come out of a storyboard
}

- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {
        // Initialization code
        [self setup];
    }
    return self;
}

#define SCALE_TO_GREEN(x) x > 5.0 ? 1.0 - (x - 5) / 5.0f : 1.0
#define SCALE_TO_RED(x) x < 5.0 ? x / 5.0f : 1.0
+ (UIColor *)colorForScale:(float)scale
{
    if (scale < 0 || scale > 10.0f) return [UIColor blackColor];
    return [UIColor colorWithRed: SCALE_TO_RED( scale) green: SCALE_TO_GREEN( scale) blue: 0.0 alpha: 1.0f];
}

- (UIColor *)getColor
{
    UIColor *c = [BIColorAlertView colorForScale: self.scale];
    if (self.scale < -0.5) c = [UIColor blackColor];
    return c;
}

- (void)drawCircleAtPoint:(CGPoint)p withRadius:(CGFloat)radius inContext:(CGContextRef)context
{
    [self drawCircleAtPoint: p withRadius: radius inContext: context withStroke: YES withColor: [UIColor blackColor] withFill: YES withColor: [self getColor]];
}

- (void)drawCircleAtPoint:(CGPoint)p
               withRadius:(CGFloat)radius
                inContext:(CGContextRef)context
               withStroke:(BOOL)wantsStroke withColor:(UIColor *)scolor
                 withFill:(BOOL)wantsFill withColor:(UIColor *)fcolor
{
    UIGraphicsPushContext(context);
    CGContextBeginPath(context);
    CGContextAddArc(context, p.x, p.y, radius, 0, 2*M_PI, YES); // 360 degree (0 to 2pi) arc
    CGContextClosePath( context);
    
    if (wantsStroke)
    {
        CGContextSetStrokeColorWithColor( context, [scolor CGColor]);
    }
    if (wantsFill)
    {
        CGContextSetFillColorWithColor( context, [fcolor CGColor]);
    }
    
    CGContextDrawPath( context, kCGPathFillStroke);
    UIGraphicsPopContext();
}

- (void)drawRect:(CGRect)rect
{
    
    CGContextRef context = UIGraphicsGetCurrentContext();
    
    CGPoint midPoint; // center of our bounds in our coordinate system
    midPoint.x = self.bounds.origin.x + self.bounds.size.width/2;
    midPoint.y = self.bounds.origin.y + self.bounds.size.height/2;
    
    CGFloat size = self.bounds.size.height / 2 - 2.0f;
    if (self.bounds.size.height < self.bounds.size.width) size = self.bounds.size.height / 2;
    
    [self drawCircleAtPoint:midPoint withRadius:size inContext:context]; // head
}


@end
