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
        store.fetchRecentPhotos() {
            (PhotosResult) -> Void in
            switch PhotosResult {
            case let .Success(photos):
                print("Successfully found \(photos.count) recent photos")

                if let firstPhoto = photos.first {
                    self.store.fetchImageForPhoto(firstPhoto) {
                        (imageResult) -> Void in
                        switch imageResult {
                        case let .Success(image):
                            NSOperationQueue.mainQueue().addOperationWithBlock{
                                self.imageView.image = image
                            }
                        case let .Failure(error):
                            print("Error downloading image: \(error)")
                        }
                    }
                }
            case let .Failure(error):
                print("Error Fetching recent photos \(error)")

            }
        }
    }
}
