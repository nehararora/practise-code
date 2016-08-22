//
//  Photo.swift
//  Photorama
//
//  Created by Nehar Arora on 8/20/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import Foundation

class Photo {
    let title: String
    let photoId: String
    let remoteURL: NSURL
    let dateTaken: NSDate

    init(title: String, photoId: String, remoteURL:NSURL, dateTaken: NSDate) {
        self.title = title
        self.photoId = photoId
        self.remoteURL = remoteURL
        self.dateTaken = dateTaken
    }
}