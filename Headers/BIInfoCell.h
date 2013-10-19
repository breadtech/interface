//
//  BIInfoCell.h
//  breadgrader
//
//  Created by Brian Kim on 3/24/13.
//  Copyright (c) 2013 bread. All rights reserved.
//

/*********************/

#import <UIKit/UIKit.h>

#define InfoCellTypeIdentifierFill @"info-fill";
#define InfoCellTypeIdentifierFill2 @"info-fill2";
#define InfoCellTypeIdentifierTextView @"info-textview";
#define InfoCellTypeIdentifierPicker @"info-picker";

typedef enum {
    InfoTypeFill,
    InfoTypeFill2,
    InfoTypeTextView,
    InfoTypePicker
} InfoType;

@interface BIInfoCell : UITableViewCell

@property (nonatomic) InfoType type;

@property (nonatomic, strong) UITextField *textField1;
@property (nonatomic, strong) UITextField *textField2;
@property (nonatomic, strong) UITextView *textView;

- (id)initWithType:(InfoType)type;
- (id)initWithType:(InfoType)type andCellStyle:(UITableViewCellStyle)style;

+ (NSString *)cellIdentifierForInfoCellType:(InfoType)type;

@end
