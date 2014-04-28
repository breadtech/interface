//
//  BITableViewController.h
//  breadinterface
//
//  Created by Brian Kim on 10/19/13.
//  Copyright (c) 2013 breadtech. All rights reserved.
//

#import "BIViewController.h"

@interface BITableViewController : BIViewController <UITableViewDataSource, UITableViewDelegate>
@property (nonatomic, strong) UITableView *tableView;
@property (nonatomic) BOOL wantsGroupedStyle;
@end
