//
//  BGListViewController.m
//  breadgrader
//
//  Created by Brian Kim on 3/6/13.
//  Copyright (c) 2013 bread. All rights reserved.
//

#import "BIListViewController.h"
#import "BIListCell.h"

@interface BIListViewController ()
@end

@implementation BIListViewController

#pragma mark - BIListVC Public API

// sample implementation
- (void)cell:(BIListCell *)cell atIndexPath:(NSIndexPath *)ip
{
    cell.alert.scale = 0.0;
    cell.textLabel.text = @"a list cell";
}

#pragma mark - UITableViewController methods

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *identifier = @"list cell";
    BIListCell *cell = [tableView dequeueReusableCellWithIdentifier: identifier];
    if (!cell)
    {
        cell = [[BIListCell alloc] initWithStyle: UITableViewCellStyleValue1 reuseIdentifier: identifier];
    }
    
    [self cell: cell atIndexPath: indexPath];
    
    return cell;
}

@end
