//
//  BIShareableItem.h
//  breadInterface
//
//  Created by Brian Kim on 10/10/13.
//  Copyright (c) 2013 breadtech. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface BIShareableItem : NSObject

@property (nonatomic, retain) NSString *title;
@property (nonatomic, retain) NSString *shortDescription;
@property (nonatomic, retain) NSString *description;

@property (nonatomic, retain) NSString *imageURLString;
@property (nonatomic, retain) NSString *itemURLString;

- (id)initWithTitle:(NSString *)title;

@end
