//
//  BIListViewController+CoreDataFetch.h
//  breadinterface
//
//  Created by Brian Kim on 10/19/13.
//  Copyright (c) 2013 breadtech. All rights reserved.
//

#import "BIListViewController.h"
#import <CoreData/CoreData.h>

@interface BIListViewController (CoreDataFetch) <NSFetchedResultsControllerDelegate>

@property (nonatomic, strong) NSFetchedResultsController *frc;
@property (nonatomic, strong) NSManagedObjectContext *moc;

- (void)performFetch;

@end
