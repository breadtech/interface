//
//  BIViewController.h
//  breadgrader
//
//  Created by Brian Kim on 7/27/13.
//  Copyright (c) 2013 breadtech. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "BIShareableItem.h"

@interface BIViewController : UIViewController

@property (nonatomic, weak) id<UIApplicationDelegate> appDelegate;
@property (nonatomic, strong) BIShareableItem *shareableItem;

// main control buttons
@property (nonatomic, strong) UIBarButtonItem *tl;
@property (nonatomic, strong) UIBarButtonItem *tr;
@property (nonatomic, strong) UIBarButtonItem *bl;
@property (nonatomic, strong) UIBarButtonItem *br;
@property (nonatomic) BOOL wantBottomMiddleButton;

// UIBarButtonItem convenience properties
@property (nonatomic, strong) UIBarButtonItem *addButton;
@property (nonatomic, strong) UIBarButtonItem *archiveButton;
@property (nonatomic, strong) UIBarButtonItem *backButton;
@property (nonatomic, strong) UIBarButtonItem *bottomMiddleButton;
@property (nonatomic, strong) UIBarButtonItem *cancelButton;
@property (nonatomic, strong) UIBarButtonItem *closeButton; 
@property (nonatomic, strong) UIBarButtonItem *deleteButton;
@property (nonatomic, strong) UIBarButtonItem *doneButton;
@property (nonatomic, strong) UIBarButtonItem *helpButton;
@property (nonatomic, strong) UIBarButtonItem *infoButton;
@property (nonatomic, strong) UIBarButtonItem *menuButton;
@property (nonatomic, strong) UIBarButtonItem *noButton; // a blank button
@property (nonatomic, strong) UIBarButtonItem *searchButton;
@property (nonatomic ,strong) UIBarButtonItem *settingsButton;
@property (nonatomic, strong) UIBarButtonItem *shareButton;

// calls:
- (void)addButtonPressed:(id)sender;
- (void)archiveButtonPressed:(id)sender;
- (void)backButtonPressed:(id)sender;
- (void)bottomMiddleButtonPessed:(id)sender;
- (void)cancelButtonPressed:(id)sender;
- (void)closeButtonPressed:(id)sender;
- (void)deleteButtonPressed:(id)sender;
- (void)doneButtonPressed:(id)sender;
- (void)helpButtonPressed:(id)sender;
- (void)infoButtonPressed:(id)sender;
- (void)menuButtonPressed:(id)sender;
- (void)settingsButtonPressed:(id)sender;
- (void)searchButtonPressed:(id)sender;
- (void)searchButtonLongPressed:(id)sender;
- (void)shareButtonPressed:(id)sender;

// lifecycle methods
- (id)init;         // this view controller is best used without a storyboard or xib, just use init
- (void)setupModel; // abstract: setup your own model
- (void)setupUI;    // call super at the end

// by convention, the model should update first and then the UI
- (void)updateModel;// call whenever you want to fetch ui data into your model
- (void)updateUI;   // call whenever your model is updated

// only call this method
- (void)cleanup;

// override these and call super
- (void)cleanupUI;
- (void)cleanupModel;

// toolbar methods


@end
