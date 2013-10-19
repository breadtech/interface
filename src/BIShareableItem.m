//
//  BIShareableItem.m
//  breadInterface
//
//  Created by Brian Kim on 10/10/13.
//  Copyright (c) 2013 breadtech. All rights reserved.
//

#import "BIShareableItem.h"

@implementation BIShareableItem

@synthesize title = _title;
@synthesize shortDescription = _shortDescription;
@synthesize description = _description;
@synthesize imageURLString = _imageURLString;
@synthesize itemURLString = _itemURLString;

- (id)initWithTitle:(NSString *)title {
    self = [super init];
    if (self!=nil) {
        [self setTitle:title];
    }
    return self;
}

- (void)dealloc {
    
    [self setTitle:nil];
    [self setShortDescription:nil];
    [self setDescription:nil];
    [self setImageURLString:nil];
    [self setItemURLString:nil];
}

@end
