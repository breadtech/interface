//
//  BITableViewController.m
//  breadinterface
//
//  Created by Brian Kim on 10/19/13.
//  Copyright (c) 2013 breadtech. All rights reserved.
//

#import "BITableViewController.h"

@interface BITableViewController ()

@end

@implementation BITableViewController

#pragma mark - UITableView property

- (UITableView *)tableView
{
    if (!_tableView)
    {
        _tableView = [[UITableView alloc] initWithFrame: self.view.frame
                                                  style: UITableViewStylePlain];
        _tableView.autoresizingMask = UIViewAutoresizingFlexibleHeight | UIViewAutoresizingFlexibleWidth;

        _tableView.dataSource = self;
        _tableView.delegate = self;
    }
    return _tableView;
}

#pragma mark - UITableView protocol methods

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section { return 1; }
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *cellidentifier = @"cell";
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier: cellidentifier];
    if (!cell) {
        cell = [[UITableViewCell alloc] initWithStyle: UITableViewCellStyleDefault reuseIdentifier: cellidentifier];
    }
    
    cell.textLabel.text = @"this is a table view cell";
    
    return cell;
}

#pragma mark - BIViewController methods

- (void)setupUI
{

    
    [self.view addSubview: self.tableView];
    
    [super setupUI];
}

- (void)updateUI
{
    [self.tableView reloadData];
    
    [super updateUI];
}

@end
