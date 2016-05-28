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

    func setImage(image: UIImage, forKey key:String) {
        cache.setObject(image, forKey: key)
    }

    func imageForKey(key: String) -> UIImage? {
        return cache.objectForKey(key) as? UIImage
    }

    func deleteForKey(key:String) {
        cache.removeObjectForKey(key)
    }
}
