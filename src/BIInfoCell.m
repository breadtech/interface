//
//  BIInfoCell.m
//  breadgrader
//
//  Created by Brian Kim on 3/24/13.
//  Copyright (c) 2013 bread. All rights reserved.
//

#import "BIInfoCell.h"

@interface BIInfoCell()
@end

@implementation BIInfoCell

#define TEXTFIELD_FRAME CGRectMake( 110.0f, 11.0f, 210.0f, 20.0f)

+ (UITextField *)aTextField
{
    UITextField *tf = [[UITextField alloc] initWithFrame: TEXTFIELD_FRAME];
    tf.clearButtonMode = UITextFieldViewModeWhileEditing;
    tf.borderStyle = UITextBorderStyleNone;
    tf.font = [UIFont boldSystemFontOfSize: 15.0f];
    tf.enabled = YES;
    tf.autoresizingMask = UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleRightMargin;
    tf.returnKeyType = UIReturnKeyDone;
    return tf;
}

- (id)initWithType:(InfoType)type andCellStyle:(UITableViewCellStyle)style
{
    
    NSString *identifier = [BIInfoCell cellIdentifierForInfoCellType: type];
    self = [self initWithStyle: style reuseIdentifier: identifier];
    
    if (self) {
        // todo: use autolayout to dynamically extend the detailTextLabel based on the length of its text
        self.type = type;
        
        if (self.type == InfoTypeFill)
        {
            self.textField1 = [BIInfoCell aTextField];
            [self.contentView addSubview: self.textField1];
        }
        else if (self.type == InfoTypeFill2)
        {
            UITextField *tf1 = [BIInfoCell aTextField];
            CGRect tf1Frame = tf1.frame;
            tf1Frame.size.width = 90.0f;
            tf1.frame = tf1Frame;
            self.textField1 = tf1;
            
#define DIVIDER_FRAME CGRectMake( 200.0f, 0, 1.0f, 43.0f)
            
            UIView *divider = [[UIView alloc] initWithFrame: DIVIDER_FRAME];
            divider.backgroundColor = [UIColor groupTableViewBackgroundColor];
            divider.autoresizingMask = UIViewAutoresizingFlexibleLeftMargin | UIViewAutoresizingFlexibleRightMargin;
            
            CGRect tf2Frame = tf1Frame;
            tf2Frame.origin.x = 212.0f;
            UITextField *tf2 = [BIInfoCell aTextField];
            tf2.frame = tf2Frame;
            tf2.autoresizingMask = UIViewAutoresizingFlexibleLeftMargin | UIViewAutoresizingFlexibleWidth;
            self.textField2 = tf2;
            
            [self.contentView addSubview: tf1];
            [self.contentView addSubview: tf2];
            [self.contentView addSubview: divider];
        }
        else if (self.type == InfoTypeTextView)
        {
            CGRect cellFrame = self.contentView.frame;
            UITextView *tv = [[UITextView alloc] initWithFrame: CGRectMake(cellFrame.origin.x + 110.0,
                                                                          cellFrame.origin.y + 10.0,
                                                                          cellFrame.size.width - 95.0,
                                                                          25.0)];
            tv.font = [UIFont boldSystemFontOfSize:15.0];
            tv.editable = YES;
            tv.backgroundColor = [UIColor clearColor];
            tv.autoresizingMask = UIViewAutoresizingFlexibleWidth;
            self.textView = tv;
            
            [self.contentView addSubview:tv];
            
        }
        else if (self.type == InfoTypePicker)
        {
            self.accessoryType = UITableViewCellAccessoryDisclosureIndicator;
        }
        self.selectionStyle = UITableViewCellSelectionStyleGray;
    }
    return self;

}

- (id)initWithType:(InfoType)type
{
    return [self initWithType: type andCellStyle: UITableViewCellStyleValue2];
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated
{
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
    
}

+ (NSString *)cellIdentifierForInfoCellType:(InfoType)type
{
    NSString *ret = @"";
    if (type == InfoTypeFill)
    {
        ret = InfoCellTypeIdentifierFill;
    } else if (type == InfoTypeFill2)
    {
        ret = InfoCellTypeIdentifierFill2;
    } else if (type == InfoTypePicker)
    {
        ret = InfoCellTypeIdentifierPicker;
    } else if (type == InfoTypeTextView)
    {
        ret = InfoCellTypeIdentifierTextView;
    }
    return ret;
}

@end
