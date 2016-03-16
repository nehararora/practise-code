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
        var url: String = "http://​www.bignerdranch.com"
        print("URL is \(url)")
        let request = NSURLRequest(URL: url!)
        webView.loadRequest(request)
    }

}
