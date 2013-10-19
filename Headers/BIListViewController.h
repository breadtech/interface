//
//  BIListViewController.h
//  breadgrader
//
//  Created by Brian Kim on 3/6/13.
//  Copyright (c) 2013 bread. All rights reserved.
//

#import "BITableViewController.h"

//
//  name = BIListViewController
//  inherits = BITableViewController
//

@class BIListCell;

@interface BIListViewController : BITableViewController

//
// ListViewController public instance methods
//

// override = true
- (void)cell:(BIListCell *)cell atIndexPath:(NSIndexPath *)ip;

@end
