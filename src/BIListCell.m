//
//  BGListCell.m
//  breadgrader
//
//  Created by Brian Kim on 3/6/13.
//  Copyright (c) 2013 bread. All rights reserved.
//

#import "BIListCell.h"

@implementation BIListCell

- (id)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier
{
    BIListCell *cell = [super initWithStyle: style reuseIdentifier: reuseIdentifier];
    
    cell.imageView.image = [UIImage imageNamed: @"blank.png"];
    
    self.alert = [[BIColorAlertView alloc] initWithFrame: CGRectMake( 11, 11, 22, 22)];
    [cell.imageView addSubview: self.alert];
    
    return cell;
}

@end
