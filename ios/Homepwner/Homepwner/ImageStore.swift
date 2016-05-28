//
//  ImageStore.swift
//  Homepwner
//
//  Created by Nehar Arora on 5/27/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class ImageStore {
    let cache = NSCache()

    // MARK: - CRUD operations
    func setImage(image: UIImage, forKey key:String) {
        cache.setObject(image, forKey: key)

        // create url for image
        let imageURL = imageURLForKey(key)
        if let data = UIImagePNGRepresentation(image) {
            data.writeToURL(imageURL, atomically: true)
        }
    }

    func imageForKey(key: String) -> UIImage? {
        // check for cached image first
        if let existingImage = cache.objectForKey(key) as? UIImage {
            return existingImage
        }

        let imageURL = imageURLForKey(key)

        guard let imagefromDisk = UIImage(contentsOfFile: imageURL.path!) else {
            return nil
        }
        cache.setObject(imagefromDisk, forKey: key)
        return imagefromDisk

    }

    func deleteForKey(key:String) {
        // remove from cache...
        cache.removeObjectForKey(key)

        // and disk
        let imageURL = self.imageURLForKey(key)
        do {
            try NSFileManager.defaultManager().removeItemAtURL(imageURL)
        } catch let deleteError {
            print("Error removing image from disk \(deleteError)")
        }


    }

    // MARK: - Utility methods
    func imageURLForKey(key: String) -> NSURL {
        let documentDirectories = NSFileManager.defaultManager().URLsForDirectory(.DocumentDirectory, inDomains: .UserDomainMask)
        let documentDirectory = documentDirectories.first!
        return documentDirectory.URLByAppendingPathComponent(key)
    }
}
