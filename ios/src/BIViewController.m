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

@interface BIViewController () <UIActionSheetDelegate, MFMailComposeViewControllerDelegate, MFMessageComposeViewControllerDelegate>
@property (nonatomic, strong) UIBarButtonItem *flexBar;
@end

@implementation BIViewController
@synthesize tl = _tl;
@synthesize tr = _tr;
@synthesize bl = _bl;
@synthesize br = _br;

#pragma mark - Public API

- (id)appDelegate
{
    return [[UIApplication sharedApplication] delegate];
}

- (id)init
{
    self = [super init];
    if (self)
    {
    }
    return self;
}

#pragma mark - main bar button properties

- (UIBarButtonItem *)tl
{
    if (!_tl)
    {
        _tl = self.noButton;
    }
    return _tl;
}

- (void)setTl:(UIBarButtonItem *)tl
{
    if (_tl != tl)
    {
        _tl = tl;
        [self updateToolbars];
    }
}

- (UIBarButtonItem *)tr
{
    if (!_tr)
    {
        _tr = self.noButton;
    }
    return _tr;
}

- (void)setTr:(UIBarButtonItem *)tr
{
    if (_tr != tr)
    {
        _tr = tr;
        [self setupToolbars];
    }
    
}

- (UIBarButtonItem *)bl
{
    if (!_bl)
    {
        _bl = self.noButton;
    }
    return _bl;
}

- (void)setBl:(UIBarButtonItem *)bl
{
    if (_bl != bl)
    {
        _bl = bl;
        [self setupToolbars];
    }
}

- (UIBarButtonItem *)br
{
    if (!_br)
    {
        _br = self.noButton;
    }
    return _br;
}

- (void)setBr:(UIBarButtonItem *)br
{
    if (_br != br)
    {
        _br = br;
        [self setupToolbars];
    }
    
}

#pragma mark - bar button properties

- (UIBarButtonItem *)addButton
{
    if (!_addButton)
    {
        _addButton = [UIBarButtonItem barButtonItemWithUnicode: [UnicodeDictionary dictionary][@"plus"]
                                                         target: self
                                                         action: @selector( addButtonPressed:)];
    }
    return _addButton;
}

- (UIBarButtonItem *)archiveButton
{
    if (!_archiveButton)

    {
        _archiveButton = [UIBarButtonItem barButtonItemWithUnicode: [UnicodeDictionary dictionary][@"folder"]
                                                            target: self
                          
                                                            action: @selector( archiveButtonPressed:)];
    }
    return _archiveButton;
}

- (UIBarButtonItem *)backButton
{
    if (!_backButton)
    {
        _backButton = [UIBarButtonItem barButtonItemWithUnicode: [UnicodeDictionary dictionary][@"back"]
                                                         target: self
                                                         action: @selector( backButtonPressed:)];

    }
    return _backButton;
    
}

- (UIBarButtonItem *)bottomMiddleButton
{
    if (!_bottomMiddleButton)
    {
        _bottomMiddleButton = [[UIBarButtonItem alloc] initWithTitle: @"Middle Button"
                                                               style: UIBarButtonItemStyleBordered
                                                              target: self
                                                              action: @selector( bottomMiddleButtonPessed:)];
    }
    return _bottomMiddleButton;
}

- (UIBarButtonItem *)cancelButton
{
    if (!_cancelButton)
    {
        _cancelButton = [UIBarButtonItem barButtonItemWithUnicode: [UnicodeDictionary dictionary][@"close"]
                                                           target: self
                                                           action: @selector( cancelButtonPressed:)];

    }
    return _cancelButton;
}

- (UIBarButtonItem *)closeButton
{
    if (!_closeButton)
    {
        _closeButton = [UIBarButtonItem barButtonItemWithUnicode: [UnicodeDictionary dictionary][@"close"]
                                                          target: self
                                                          action: @selector( closeButtonPressed:)];

    }
    return _closeButton;
}

- (UIBarButtonItem *)deleteButton
{
    if (!_deleteButton)
    {
        _deleteButton = [[UIBarButtonItem alloc] initWithBarButtonSystemItem: UIBarButtonSystemItemTrash
                                           target: self
                                           action: @selector( deleteButtonPressed:)];
;
    }
    return _deleteButton;
    
}

- (UIBarButtonItem *)doneButton
{
    if (!_doneButton)
    {
        _doneButton = [UIBarButtonItem barButtonItemWithUnicode: [UnicodeDictionary dictionary][@"done"]
                                                         target: self
                                                         action: @selector( doneButtonPressed:)];
    }
    return _doneButton;
}

- (UIBarButtonItem *)helpButton
{
    if (!_helpButton)
    {
        _helpButton = [UIBarButtonItem barButtonItemWithUnicode: [UnicodeDictionary dictionary][@"help"] target: self action: @selector( helpButtonPressed:)];
    }
    return _helpButton;
}

- (UIBarButtonItem *)infoButton
{
    if (!_infoButton)
    {
        _infoButton = [UIBarButtonItem barButtonItemWithUnicode: [UnicodeDictionary dictionary][@"info"]
                                                         target: self
                                                         action: @selector( infoButtonPressed:)];
    }
    return _infoButton;
}

- (UIBarButtonItem *)noButton
{
    if (!_noButton)
    {
        _noButton = [[UIBarButtonItem alloc] initWithCustomView: [UIView new]];
    }
    return _noButton;
}

- (UIBarButtonItem *)menuButton
{
    if (!_menuButton)
    {
        _menuButton = [UIBarButtonItem barButtonItemWithUnicode: [UnicodeDictionary dictionary][@"menu"]
                                                         target: self
                                                         action: @selector( menuButtonPressed:)];
        /*
        _menuButton = [UIBarButtonItem barItemWithImage: [UIImage imageNamed: @"menu.icon.png"]
                                                  target: self
                                                  action: @selector( menuButtonPressed:)];*/
    }
    return _menuButton;
}

- (UIBarButtonItem *)searchButton
{
    if (!_searchButton)
    {
        _searchButton = [UIBarButtonItem barItemWithImage: [UIImage imageNamed: @"search.icon.png"]
                                                   target: self action: @selector( searchButtonPressed:)];
    }
    return _searchButton;
}

- (UIBarButtonItem *)settingsButton
{
    if (!_settingsButton)
    {
        _settingsButton = [UIBarButtonItem barButtonItemWithUnicode: [UnicodeDictionary dictionary][@"gear"]
                                                     target: self
                                                     action: @selector( settingsButtonPressed:)];
    }
    return _settingsButton;
}

- (UIBarButtonItem *)shareButton
{
    if (!_shareButton)
    {
        _shareButton = [UIBarButtonItem barButtonItemWithUnicode: [UnicodeDictionary dictionary][@"share"]
                                                          target: self
                                                          action: @selector( shareButtonPressed:)];
    }
    return _shareButton;
}

- (UIBarButtonItem *)flexBar
{
    if (!_flexBar)
    {
        _flexBar = [[UIBarButtonItem alloc] initWithBarButtonSystemItem: UIBarButtonSystemItemFlexibleSpace
                                                                 target: nil
                                                                 action: nil];
    }
    return _flexBar;
}

- (BIShareableItem *)shareableItem
{
    if (!_shareableItem)
    {
        _shareableItem = [[BIShareableItem alloc] initWithTitle: @"breadinterface"];
        _shareableItem.shortDescription = @"breadinterface is great. All I have to do is learn how to use it once and then I'll know how to use it anywhere!";
        _shareableItem.description = @"http://interface.breadtech.com";
    }
    return _shareableItem;
}

#pragma mark - button calls

- (void)addButtonPressed:(id)sender {}
- (void)archiveButtonPressed:(id)sender {}
- (void)backButtonPressed:(id)sender { [self popVC]; }
- (void)bottomMiddleButtonPessed:(id)sender {}
- (void)cancelButtonPressed:(id)sender { [self cancel: sender]; }
- (void)closeButtonPressed:(id)sender { [self close: sender]; }
- (void)deleteButtonPressed:(id)sender { [self confirmDelete: sender]; }
- (void)doneButtonPressed:(id)sender {}
- (void)helpButtonPressed:(id)sender {}
- (void)infoButtonPressed:(id)sender {}
- (void)menuButtonPressed:(id)sender {}
- (void)searchButtonPressed:(id)sender {}
- (void)searchButtonLongPressed:(id)sender {}
- (void)settingsButtonPressed:(id)sender {}
- (void)shareButtonPressed:(id)sender { [self showShareMenu: sender]; }

#pragma mark - convenience methods methods

- (void)cancel:(id)sender
{
    if (self.view.window) [self.navigationController popViewControllerAnimated: YES];
}

- (void)close:(id)sender
{
    [self.navigationController dismissViewControllerAnimated: YES completion: nil];
}

- (void)confirmDelete:(id)sender
{
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle: @"Confirm Delete" message: @"Are you sure you want to delete this item?" delegate: self cancelButtonTitle: @"No" otherButtonTitles: @"Delete", nil];
    [alert show];
}

- (void)popVC
{
    [self.navigationController popViewControllerAnimated: YES];
}

- (void)mailComposeController:(MFMailComposeViewController *)controller didFinishWithResult:(MFMailComposeResult)result error:(NSError *)error
{
    [self dismissViewControllerAnimated: YES completion: nil];
}

- (void)messageComposeViewController:(MFMessageComposeViewController *)controller didFinishWithResult:(MessageComposeResult)result
{
    [self dismissViewControllerAnimated: YES completion: nil];
}

- (void)actionSheet:(UIActionSheet *)actionSheet clickedButtonAtIndex:(NSInteger)buttonIndex
{
    NSString *service = [actionSheet buttonTitleAtIndex: buttonIndex];
    NSString *msg = [NSString stringWithFormat: @"%@ %@", self.shareableItem.shortDescription, self.shareableItem.description];
    UIViewController *vc;
    if ([service isEqualToString: @"Mail"])
    {
        if ([MFMailComposeViewController canSendMail])
        {
            MFMailComposeViewController *mailvc = [[MFMailComposeViewController alloc] init];
            [mailvc setMessageBody: msg isHTML: NO];
            mailvc.mailComposeDelegate = self;
            vc = mailvc;
        } else
        {
            
            UIAlertView *alert = [[UIAlertView alloc] initWithTitle: @"You can't send mail!"
                                                            message: @"Try again when you are signed into Mail or have a working Internet connection"
                                                           delegate: nil
                                                  cancelButtonTitle: @"OK"
                                                  otherButtonTitles: nil];
            [alert show];
        }
    } else if ([service isEqualToString: @"Message"])
    {
        if ([MFMessageComposeViewController canSendText])
        {
            MFMessageComposeViewController *messagevc = [[MFMessageComposeViewController alloc] init];
            [messagevc setBody: msg];
            messagevc.messageComposeDelegate = self;
            vc = messagevc;
        } else
        {
            UIAlertView *alert = [[UIAlertView alloc] initWithTitle: @"You can't text!"
                                                            message: @"Try again when you are signed into Messages or have a working Internet connection"
                                                           delegate: nil
                                                  cancelButtonTitle: @"OK"
                                                  otherButtonTitles: nil];
            [alert show];
        }
    } else if ([service isEqualToString: @"Twitter"])
    {
        if ([TWTweetComposeViewController canSendTweet])
        {
            TWTweetComposeViewController *twittervc = [[TWTweetComposeViewController alloc] init];
            [twittervc setInitialText: msg];
            twittervc.completionHandler = ^(TWTweetComposeViewControllerResult result)
            {
                [self dismissViewControllerAnimated: YES completion: nil];
            };
            vc = twittervc;
        } else
        {
            UIAlertView *alert = [[UIAlertView alloc] initWithTitle: @"You can't tweet!"
                                                            message: @"Try again when you are signed into Twitter or have a working Internet connection"
                                                           delegate: nil
                                                  cancelButtonTitle: @"OK"
                                                  otherButtonTitles: nil];
            [alert show];
        }
    }
    if (vc)
    {
        [self presentViewController: vc
                           animated: YES
                         completion: nil];
    }
}

- (void)showShareMenu:(id)sender
{
    if (SYSTEM_VERSION_LESS_THAN( @"6.0"))
    {
        UIActionSheet *actionsheet = [[UIActionSheet alloc] initWithTitle: @"Share with"
                                                                 delegate: self
                                                        cancelButtonTitle: @"Cancel"
                                                   destructiveButtonTitle: nil
                                                        otherButtonTitles: @"Mail", @"Message", @"Twitter", nil];
        [actionsheet showFromBarButtonItem: self.shareButton animated: YES];
    }
    else
    {
        NSArray *items = @[
                           self.shareableItem.shortDescription,
                           self.shareableItem.description
                           ];
        
        UIActivityViewController *activityvc = [[UIActivityViewController alloc] initWithActivityItems: items applicationActivities: nil];
        [self presentViewController: activityvc animated: YES completion: nil];
    }
}

- (void)motionEnded:(UIEventSubtype)motion withEvent:(UIEvent *)event
{
    if (event.subtype == UIEventSubtypeMotionShake)
    {
        [self showShareMenu: nil];
    }
}

#pragma mark - breadinterface lifecycle methods

- (void)setupModel {}

- (void)setupToolbars
{
    self.navigationController.toolbarHidden = NO;
    
    UIColor *black = [UIColor blackColor];
    UIColor *white = [UIColor whiteColor];

    if (SYSTEM_VERSION_GREATER_THAN_OR_EQUAL_TO( @"7.0"))
    {
        self.navigationController.navigationBar.barTintColor = black;
        self.navigationController.navigationBar.tintColor = white;
        self.navigationController.toolbar.barTintColor = black;
        self.navigationController.toolbar.tintColor = white;
    }
    else // iOS 6.1 or older
    {
        self.navigationController.navigationBar.tintColor = black;
        self.navigationController.toolbar.tintColor = black;
    }
    
    self.navigationController.navigationBar.titleTextAttributes = @{ UITextAttributeTextColor : white };
    
    [self updateToolbars];
}

- (void)setupUI
{
    [self setupToolbars];
    
    [self updateUI];
}

- (void)updateModel {}

- (void)updateToolbars
{
    self.navigationItem.leftBarButtonItem = self.tl;
    self.navigationItem.rightBarButtonItem = self.tr;
    
    NSMutableArray *toolbarItems = [@[ self.bl, self.flexBar ] mutableCopy];
    if (self.wantBottomMiddleButton) {[toolbarItems addObjectsFromArray: @[ self.bottomMiddleButton, self.flexBar ]];}
    [toolbarItems addObject: self.br];
    self.toolbarItems = toolbarItems;
}

- (void)updateUI {}

- (void)cleanup
{
    [self cleanupUI];
    [self cleanupModel];
}

- (void)cleanupUI
{
    self.tl = nil;
    self.tr = nil;
    self.bl = nil;
    self.br = nil;
}

- (void)cleanupModel
{
    
}

- (void)toggleButtons:(BOOL)on
{
    self.tl.enabled = self.tr.enabled = self.bl.enabled = self.br.enabled = on;
}

#pragma mark - UIViewController methods

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear: animated];
    [self setupModel];
    [self setupUI];
    
    [self toggleButtons: NO];
}

- (void)viewDidAppear:(BOOL)animated
{
    [super viewDidAppear: animated];
    
    [self toggleButtons: YES];
}

- (void)viewDidUnload
{
    [self cleanup];
    [super viewDidUnload];
}

- (void)viewWillDisappear:(BOOL)animated
{
    [self cleanup];
    [super viewWillDisappear: animated];
}

- (void)viewWillUnload
{
    [self cleanup];
    [super viewWillUnload];
}

- (void)dealloc
{
    [self cleanup];
}

- (BOOL)canBecomeFirstResponder
{
    return YES;
}

@end
