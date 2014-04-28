//
//  UnicodeDictionary.m
//  breadbank
//
//  Created by Brian Kim on 10/19/13.
//  Copyright (c) 2013 breadtech. All rights reserved.
//

#import "UnicodeDictionary.h"

#import <Foundation/Foundation.h>


@implementation UnicodeDictionary

static NSDictionary *dictionary;

+ (NSDictionary *)dictionary
{
    if (dictionary == nil) {
        dictionary = @{
                       @"close" : @"\u274C",
                       @"help" : @"\u2754",
                       @"warning" : @"\u26A0",
                       @"error" : @"\u26D4",
                       @"moneybag" : @"\U0001F4B0",
                       @"100%" : @"\U0001F4AF",
                       @"chatbubble" : @"\U0001F4AC",
                       @"floppydisk" : @"\U0001F4BE",
                       @"computer" : @"\U0001F4BB",
                       @"clipboard" : @"\U0001F4CB",
                       @"pin" : @"\U0001F4CD",
                       @"share" : @"\U0001F4E4",
                       @"camera" : @"\U0001F4F7",
                       @"search" : @"\U0001F50D",
                       @"lock" : @"\U0001F512",
                       @"unlock" : @"\U0001F513",
                       @"calendar" : @"\U0001F4C5",
                       @"poop" : @"\U0001F4A9",
                       @"back" : @"\U0001F448",
                       @"forward" : @"\U0001F449",
                       @"up" : @"\U0001F446",
                       @"down" : @"\U0001F447",
                       @"home" : @"\U0001F3E0",
                       @"microphone" : @"\U0001F3A4",
                       @"video" : @"\U0001F3A5",
                       @"info" : @"\u2139",
                       @"star" : @"\u2B50",
                       @"folder" : @"\U0001F4C2",
                       @"sync" : @"\U0001F503",
                       @"pencil" : @"\u270F",
                       @"trash" : @"\U0001F5D1",
                       @"done" : @"\u2705",
                       @"gear" : @"\u2699",
                       @"menu" : @"\u2630",
                       @"plus" : @"\u271a",
                       @"recycle" : @"\u2672"
                       };
    }
    
    return dictionary;
    
}

@end