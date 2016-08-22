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

    func fetchRecentPhotos() {
        let url = FlickerAPI.recentPhotosURL()
        let request = NSURLRequest(URL: url)
        print("Request: \(request)")
        let task = session.dataTaskWithRequest(request) {
            (data, response, error) -> Void in

            if let jsonData = data {
                do {
                    let jsonObject: AnyObject = try NSJSONSerialization.JSONObjectWithData(jsonData, options: [])
                    print(jsonObject)
                } catch let error {
                    print("Error creating json object: \(error)")
                }
            } else if let requestError = error {
                print("Error fetching recent photos \(requestError)")
            } else {
                print("Unexpected error with the request")
            }
        }
        task.resume()
    }
}