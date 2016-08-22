//
//  PhotoStore.swift
//  Photorama
//
//  Created by Nehar Arora on 8/18/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import Foundation

class PhotoStore {
    let session: NSURLSession = {
        let config = NSURLSessionConfiguration.defaultSessionConfiguration()
        return NSURLSession(configuration: config)
    }()

    func processRecentPhotosRequest(data data: NSData?, error: NSError) -> PhotosResult {
        guard let jsonData = data else {
            return .Failure(error)
        }
        return FlickerAPI.photosFromJSONData(jsonData)
    }

    func fetchRecentPhotos(completion completion: (PhotosResult) -> Void) {
        let url = FlickerAPI.recentPhotosURL()
        let request = NSURLRequest(URL: url)
        print("Request: \(request)")
        let task = session.dataTaskWithRequest(request) {
            (data, response, error) -> Void in

            let result = self.processRecentPhotosRequest(data: data, error: error!)
            completion(result)
        }
        task.resume()
    }
}