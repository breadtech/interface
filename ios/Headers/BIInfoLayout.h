//
//  BIInfoLayout.h
//  playground
//
//  Created by Brian Kim on 7/3/13.
//  Copyright (c) 2013 breadtech. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>
#import "BIInfoCell.h"

@interface BIInfoLayout : NSObject <UITableViewDataSource>

// these are abstract properties who's getter property you must override

//
// $<NSArray> layoutKeys
// these keys will be the title that the individual cells will have
// if the first element is an NSArray, then the layout will assume multiple sections
// else if the first element is an NSString, then the layout will assume one section
//
@property (nonatomic, strong) NSArray *layoutKeys;

//
// $<NSDictionary> layoutDictionary
// each key defined in layoutKeys must point to a dictionary object
// possible key-value pairs:
// @"type": @(InfoType)
// @"keyboardType": @(UIKeyboardType)
//

#define KEYBOARD_INFO_KEY @"keyboardInfo"
#define INFO_TYPE_KEY @"type"
#define CELL_STYLE_KEY @"cell-style"

@property (nonatomic, strong) NSDictionary *layoutDictionary;

- (NSIndexPath *)indexPathForKey:(NSString *)key;

/*
- (UITextField *)textFieldForKey:(NSString *)key;
- (UITextField *)textField2ForKey:(NSString *)key;
- (UITextView *)textViewForKey:(NSString *)key;
- (UILabel *)labelForKey:(NSString *)key;
*/

// convenience class methods
+ (BIInfoLayout *)defaultLayout;

+ (NSDictionary *)layoutInfoForType:(InfoType)type;
+ (NSDictionary *)layoutInfoForType:(InfoType)type
                       andCellStyle:(UITableViewCellStyle)style;
+ (NSDictionary *)layoutInfoForType:(InfoType)type andKeyboardInfo:(id)info;

+ (NSDictionary *)defaultKeyboardInfo;
+ (NSDictionary *)keyboardInfoWithPlaceholderText:(NSString *)placeholder;
+ (NSDictionary *)keyboardInfoWithPlaceholderText:(NSString *)placeholder
                                     keyboardType:(UIKeyboardType)ktype;
+ (NSDictionary *)keyboardInfoWithPlaceholderText:(NSString *)placeholder
                                     keyboardType:(UIKeyboardType)ktype
                           autocapitalizationType:(UITextAutocapitalizationType)autocapsType;
+ (NSDictionary *)keyboardInfoWithPlaceholderText:(NSString *)placeholder
                                     keyboardType:(UIKeyboardType)ktype
                           autocapitalizationType:(UITextAutocapitalizationType)autocapsType
                               autocorrectionType:(UITextAutocorrectionType)autocorrectType;

@end
