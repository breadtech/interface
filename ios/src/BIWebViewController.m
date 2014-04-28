//
//  BIWebViewController.m
//  breadgrader
//
//  Created by Brian Kim on 7/26/13.
//  Copyright (c) 2013 breadtech. All rights reserved.
//

#import "BIWebViewController.h"

@interface BIWebViewController ()
@property (nonatomic, strong) UIWebView *webView;
@end

@implementation BIWebViewController

- (NSURL *)url
{
    if (!_url)
    {
        _url = [NSURL URLWithString: @"http://www.breadtech.com"];
    }
    return _url;
}

- (UIWebView *)webView
{
    if (!_webView)
    {
        _webView = [[UIWebView alloc] initWithFrame: self.view.frame];
    }
    return _webView;
}

- (void)setupUI
{
    [self.view addSubview: self.webView];
    
    self.tr = self.br = self.bl = self.noButton;
    
    [super setupUI];
}

- (void)setupModel
{
    [self.webView loadRequest: [NSURLRequest requestWithURL: self.url]];
}

- (void)cleanupUI
{
    self.webView = nil;
    
    [super cleanupUI];
}

- (void)cleanupModel
{
    self.url = nil;
}

@end
