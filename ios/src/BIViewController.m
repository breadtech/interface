//
//  BIViewController.m
//  breadgrader
//
//  Created by Brian Kim on 7/27/13.
//  Copyright (c) 2013 breadtech. All rights reserved.
//

#import "BIViewController.h"
#import "UIBarButtonItem+borderlessButtons.h"

#import <MessageUI/MessageUI.h>
#import <Twitter/Twitter.h>

@interface BIViewController ()

// main control buttons
@property (nonatomic, strong) UIBarButtonItem *tl;
@property (nonatomic, strong) UIBarButtonItem *tr;
@property (nonatomic, strong) UIBarButtonItem *bl;
@property (nonatomic, strong) UIBarButtonItem *bm;
@property (nonatomic, strong) UIBarButtonItem *br;

@property (nonatomic, strong) UIBarButtonItem *flexBar;
@end

@implementation BIViewController
@synthesize tl = _tl;
@synthesize tr = _tr;
@synthesize bl = _bl;
@synthesize br = _br;
@synthesize flexBar = _flexBar;

#pragma mark - convenience methods/properties

- (id)appDelegate
{
    return [[UIApplication sharedApplication] delegate];
}

- (UIBarButtonItem *)flexBar
{
    if (_flexBar == nil)
    {
        _flexBar = [[UIBarButtonItem alloc] initWithBarButtonSystemItem: UIBarButtonSystemItemFlexibleSpace
                                                                 target: nil action: nil];
    }
    return _flexBar;
}

- (void)pop
{
    [self.navigationController popViewControllerAnimated: YES];
}

- (void)push:(UIViewController *)vc
{
    [self.navigationController pushViewController: vc animated: YES];
    //[self.navigationController showViewController: vc sender: self];
}

#pragma mark - BI Lifecycle

- (id)init
{
    self = [super init];
    if (self)
    {
    }
    return self;
}

- (void)start {
    [[UIApplication sharedApplication] setStatusBarStyle: UIStatusBarStyleLightContent];
}

- (void)resume {
    [self setupToolbars];
    
    if (!self.navigationController) {
        [[[UIAlertView alloc] initWithTitle: @"BreadInterface Error"
                                    message: @"This Controller was created without a Navigator. The buttons will not show"
                                  delegate: nil cancelButtonTitle: @"OK" otherButtonTitles: nil] show];
    }
    self.view.backgroundColor = [UIColor whiteColor];
}

- (void)update {
    [self updateToolbars];
}

- (void)clear {}
- (void)pause {}
- (void)stop {}

- (void)cleanup
{
    self.tl = nil;
    self.tr = nil;
    self.bl = nil;
    self.br = nil;
}

#pragma mark - BI Button Layout

- (NSString *)tl_label { return @""; }
- (NSString *)tm_label { return @""; }
- (NSString *)tr_label { return @""; }
- (NSString *)bl_label { return @""; }
- (NSString *)bm_label { return @""; }
- (NSString *)br_label { return @""; }

- (void)tl_clicked:(id)button { NSLog( @"tl clicked"); }
- (void)tm_clicked:(id)button { NSLog( @"tm clicked"); }
- (void)tr_clicked:(id)button { NSLog( @"tr clicked"); }
- (void)bl_clicked:(id)button { NSLog( @"bl clicked"); }
- (void)bm_clicked:(id)button { NSLog( @"bm clicked"); }
- (void)br_clicked:(id)button { NSLog( @"br clicked"); }

- (UIColor *)fg { return [UIColor whiteColor]; }
- (UIColor *)bg { return [UIColor blackColor]; }

- (UIBarButtonItem *)tl
{
    if (!_tl)
    {
        _tl = [[UIBarButtonItem alloc] initWithTitle: self.tl_label style:UIBarButtonItemStylePlain
                                              target: self action: @selector(tl_clicked:)];
    }
    return _tl;
}

- (UIBarButtonItem *)tr
{
    if (!_tr)
    {
        _tr = [[UIBarButtonItem alloc] initWithTitle: self.tr_label style:UIBarButtonItemStylePlain
                                              target: self action: @selector(tr_clicked:)];
    }
    return _tr;
}

- (UIBarButtonItem *)bl
{
    if (!_bl)
    {
        _bl = [[UIBarButtonItem alloc] initWithTitle: self.bl_label style:UIBarButtonItemStylePlain
                                              target: self action: @selector(bl_clicked:)];

    }
    return _bl;
}

- (UIBarButtonItem *)bm
{
    if (!_bm)
    {
        if ([self.bm_label isEqualToString: @""])
        {
            _bm = [[UIBarButtonItem alloc] initWithBarButtonSystemItem: UIBarButtonSystemItemFlexibleSpace
                                                                target: self action: @selector( bm_clicked:)];
        } else {
            _bm = [[UIBarButtonItem alloc] initWithTitle: self.bm_label style:UIBarButtonItemStylePlain
                                                  target: self action: @selector(bm_clicked:)];
            
        }
        
    }
    return _bm;
}

- (UIBarButtonItem *)br
{
    if (!_br)
    {
        _br = [[UIBarButtonItem alloc] initWithTitle: self.br_label style:UIBarButtonItemStylePlain
                                              target: self action: @selector(br_clicked:)];
    }
    return _br;
}

- (void)setupToolbars
{
    // show the bottom toolbar
    self.navigationController.toolbarHidden = NO;

    // the tm button (title) needs to be clickable
    UITapGestureRecognizer *recog = [[UITapGestureRecognizer alloc] initWithTarget: self action: @selector(tm_clicked:)];
    [recog setNumberOfTouchesRequired:1];
    [self.navigationController.navigationItem.titleView addGestureRecognizer: recog];
    
    // top colors
    self.navigationController.navigationBar.barTintColor = self.bg;
    self.navigationController.navigationBar.tintColor = self.fg;
    
    // bottom colors
    self.navigationController.toolbar.barTintColor = self.bg;
    self.navigationController.toolbar.tintColor = self.fg;
    
    self.navigationController.navigationBar.titleTextAttributes =
    @{ NSForegroundColorAttributeName : self.fg, NSBackgroundColorAttributeName : self.bg };
    
    [self updateToolbars];
}

- (void)updateToolbars
{
    // update labels
    self.tl.title = self.tl_label;
    self.title = self.tm_label;
    self.tr.title = self.tr_label;
    self.bl.title = self.bl_label;
    self.bm.title = self.bm_label;
    self.br.title = self.br_label;
    
    // top
    self.navigationItem.leftBarButtonItem = self.tl;
    self.navigationItem.rightBarButtonItem = self.tr;
    
    // bottom
    self.toolbarItems = @[ self.bl, self.flexBar, self.bm, self.flexBar, self.br ];
    
}

#pragma mark - UIViewController methods

- (void)viewDidLoad
{
    [super viewDidLoad];
    [self start];
}

- (void)viewDidAppear:(BOOL)animated
{
    [super viewDidAppear: animated];
    [self resume];
}

- (void)viewWillDisappear:(BOOL)animated
{
    [super viewWillDisappear: animated];
    [self pause];
}

- (void)viewDidDisappear:(BOOL)animated
{
    [super viewDidDisappear: animated];
    [self stop];
}

- (void)dealloc
{
    [self cleanup];
}

@end
