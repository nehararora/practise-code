//
//  PhotosViewController.swift
//  Photorama
//
//  Created by Nehar Arora on 8/16/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class PhotosViewControler: UIViewController {
    @IBOutlet var imageView: UIImageView!
    var store: PhotoStore!


    override func viewDidLoad() {
        super.viewDidLoad()
        store.fetchRecentPhotos()
    }
}
