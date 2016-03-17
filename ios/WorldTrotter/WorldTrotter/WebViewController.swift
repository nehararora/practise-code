//
//  WebViewController.swift
//  WorldTrotter
//
//  Created by Nehar Arora on 3/15/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class WebViewController: UIViewController {
    var webView: UIWebView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        webView = UIWebView()
        view = webView

        let url = NSURL(string: "http://bignerdranch.com")
        let requestObj = NSURLRequest(URL: url!)

        webView.loadRequest(requestObj)
    }

}
