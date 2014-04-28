//
//  BIInfoLayout.m
//  playground
//
//  Created by Brian Kim on 7/3/13.
//  Copyright (c) 2013 breadtech. All rights reserved.
//

#import "BIInfoLayout.h"

#define PLACEHOLDER_KEY @"placeholder"
#define KEYBOARD_TYPE_KEY @"ktype"
#define AUTO_CAPITALIZATION_KEY @"autocapsType"
#define AUTO_CORRECTION_KEY @"autocorrectionType"

@implementation BIInfoLayout

#pragma mark - Public API

+ (BIInfoLayout *)defaultLayout
{
    BIInfoLayout *layout = [[BIInfoLayout alloc] init];
    layout.layoutKeys = @[ @"key1", @"key2", @"key3" ];
    layout.layoutDictionary = @{ @"key1" : [ BIInfoLayout layoutInfoForType: InfoTypePicker],
                                 @"key2" : [BIInfoLayout layoutInfoForType: InfoTypeFill andKeyboardInfo: [BIInfoLayout keyboardInfoWithPlaceholderText: @"this is a textfield"]],
                                 @"key3" : [BIInfoLayout layoutInfoForType:InfoTypeFill2 andKeyboardInfo: @[[BIInfoLayout keyboardInfoWithPlaceholderText: @"tf1"], [BIInfoLayout keyboardInfoWithPlaceholderText: @"tf2"]]]};
    return layout;
}

+ (NSDictionary *)layoutInfoForType:(InfoType)type
{
    return @{ INFO_TYPE_KEY : @(type) };
}

+ (NSDictionary *)layoutInfoForType:(InfoType)type andKeyboardInfo:(id)info
{
    NSMutableDictionary *dict = [[self layoutInfoForType: type] mutableCopy];
    [dict setObject: info forKey: KEYBOARD_INFO_KEY];
    return [dict copy];
}

+ (NSDictionary *)layoutInfoForType:(InfoType)type andCellStyle:(UITableViewCellStyle)style
{
    NSMutableDictionary *dict = [[self layoutInfoForType: type] mutableCopy];
    [dict setObject: @(style) forKey: CELL_STYLE_KEY];
    return [dict copy];
}

+ (NSDictionary *)defaultKeyboardInfo
{
    return [self keyboardInfoWithPlaceholderText: @"textfield"];
}

+ (NSDictionary *)keyboardInfoWithPlaceholderText:(NSString *)placeholder
{
    return [BIInfoLayout keyboardInfoWithPlaceholderText: placeholder
                                            keyboardType: UIKeyboardTypeDefault];
}

+ (NSDictionary *)keyboardInfoWithPlaceholderText:(NSString *)placeholder
                                     keyboardType:(UIKeyboardType)ktype
{
    return [BIInfoLayout keyboardInfoWithPlaceholderText: placeholder
                                            keyboardType: ktype
                                  autocapitalizationType: UITextAutocapitalizationTypeSentences];
    
}

+ (NSDictionary *)keyboardInfoWithPlaceholderText:(NSString *)placeholder
                                     keyboardType:(UIKeyboardType)ktype
                           autocapitalizationType:(UITextAutocapitalizationType)autocapsType
{
    return [BIInfoLayout keyboardInfoWithPlaceholderText: placeholder
                                            keyboardType: ktype
                                  autocapitalizationType: autocapsType
                                      autocorrectionType: UITextAutocorrectionTypeDefault];
    
}

+ (NSDictionary *)keyboardInfoWithPlaceholderText:(NSString *)placeholder
                                     keyboardType:(UIKeyboardType)ktype
                           autocapitalizationType:(UITextAutocapitalizationType)autocapsType
                               autocorrectionType:(UITextAutocorrectionType)autocorrectType
{
    return @{ PLACEHOLDER_KEY : placeholder,
              KEYBOARD_TYPE_KEY : @(ktype),
              AUTO_CAPITALIZATION_KEY : @(autocapsType),
              AUTO_CORRECTION_KEY : @(autocorrectType) };
}

- (NSIndexPath *)indexPathForKey:(NSString *)key
{
    NSIndexPath *ret = nil;
    if ([self hasOneSection])
    {
        NSInteger i = [self.layoutKeys indexOfObject: key];
        if (i != NSNotFound)
            ret = [NSIndexPath indexPathForRow: i inSection: 0];
    } else
    {
        for (int i = 0; i <  self.layoutKeys.count; i++)
        {
            NSArray *a = self.layoutKeys[i];
            for (int j = 0; j < a.count; j++)
            {
                if ([a[j] isEqualToString: key])
                {
                    ret = [NSIndexPath indexPathForRow: j inSection: i];
                }
            }
        }
    }
    return ret;
}

#pragma mark - convenience methods

- (BOOL)hasOneSection
{
    return ![self.layoutKeys[0] isKindOfClass: [NSArray class]];
}

#pragma mark - UITableView datasource

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    NSInteger ret = 0;
    if ([self hasOneSection])
        ret = 1;
    else
        ret = self.layoutKeys.count;
    return ret;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    NSInteger ret = 0;
    if ([self hasOneSection])
    {
        ret = self.layoutKeys.count;
    }
    else
    {
        ret = [self.layoutKeys[section] count];
    }
    return ret;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    id obj = self.layoutKeys[indexPath.section];
    
    NSString *key;
    if ([self hasOneSection])
    {
        key = self.layoutKeys[indexPath.row];
    } else
    {
        key = obj[indexPath.row];
    }
    
    NSDictionary *info = self.layoutDictionary[key];
    InfoType type = [info[INFO_TYPE_KEY] intValue];
    NSString *identifier = [BIInfoCell cellIdentifierForInfoCellType: type];
    
    BIInfoCell *cell = (BIInfoCell *)[tableView dequeueReusableCellWithIdentifier: identifier];
    if (!cell)
    {
        NSNumber *style = info[CELL_STYLE_KEY];
        if (style)
            cell = [[BIInfoCell alloc] initWithType: type andCellStyle: style.intValue];
        else cell = [[BIInfoCell alloc] initWithType: type];
    }
    cell.textLabel.text = key;
    
    id keyboardInfo = info[KEYBOARD_INFO_KEY];
    if ([keyboardInfo isKindOfClass: [NSDictionary class]])
    {
        UIKeyboardType ktype = [keyboardInfo[KEYBOARD_TYPE_KEY] intValue];
        UITextAutocapitalizationType autocapsType = [keyboardInfo[AUTO_CAPITALIZATION_KEY] intValue];
        UITextAutocorrectionType autocorrectType = [keyboardInfo[AUTO_CORRECTION_KEY] intValue];
        NSString *placeholderText = keyboardInfo[PLACEHOLDER_KEY];
        
        if (cell.type == InfoTypeFill)
        {
            cell.textField1.keyboardType = ktype;
            cell.textField1.autocapitalizationType = autocapsType;
            cell.textField1.autocorrectionType = autocorrectType;
            cell.textField1.placeholder = placeholderText;
        }
        else if (cell.type == InfoTypeTextView)
        {
            cell.textView.keyboardType = ktype;
            cell.textView.autocapitalizationType = autocapsType;
            cell.textView.autocorrectionType = autocorrectType;
        }
    }
    else if ([keyboardInfo isKindOfClass: [NSArray class]])
    {
        NSDictionary *d1 = keyboardInfo[0];
        NSDictionary *d2 = keyboardInfo[1];
        
        cell.textField1.keyboardType = [d1[KEYBOARD_TYPE_KEY] intValue];
        cell.textField1.autocapitalizationType = [d1[AUTO_CAPITALIZATION_KEY] intValue];
        cell.textField1.autocorrectionType = [d1[AUTO_CORRECTION_KEY] intValue];
        cell.textField1.placeholder = d1[PLACEHOLDER_KEY];
        
        cell.textField2.keyboardType = [d2[KEYBOARD_TYPE_KEY] intValue];
        cell.textField2.autocapitalizationType = [d2[AUTO_CAPITALIZATION_KEY] intValue];
        cell.textField2.autocorrectionType = [d2[AUTO_CORRECTION_KEY] intValue];
        cell.textField2.placeholder = d2[PLACEHOLDER_KEY];
    }
    
    return cell;
}

@end
