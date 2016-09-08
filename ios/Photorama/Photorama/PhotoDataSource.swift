//
//  PhotoDataSource.swift
//  Photorama
//
//  Created by Nehar Arora on 8/29/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class PhotoDataSource: NSObject, UICollectionViewDataSource {

    var photos = [Photo]()

    func collectionView(collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        print("photos Count: \(photos.count)")
        guard photos.count > 0 else {
        return 0
        }
        return photos.count

    }
/*
    func numberOfSectionsInCollectionView(collectionView: UICollectionView) -> Int {
        guard photos.count > 0 else{
            return 1
        }
        // TODO: insert sections?
        return photos.count/4
    }
*/
    func collectionView(collectionView: UICollectionView, cellForItemAtIndexPath indexPath: NSIndexPath) -> UICollectionViewCell {
        let identifier = "UICollectionViewCell"
        let cell = collectionView.dequeueReusableCellWithReuseIdentifier(identifier, forIndexPath: indexPath) as! PhotoCollectionViewCell

        let photo = photos[indexPath.row]
        cell.updateWithImage(photo.image)
        return cell
    }

}
