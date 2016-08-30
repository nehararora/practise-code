//
//  PhotoStore.swift
//  Photorama
//
//  Created by Nehar Arora on 8/18/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

enum ImageResult {
    case Success(UIImage)
    case Failure(ErrorType)
}

enum PhotoError: ErrorType {
    case ImageCreationError
}

class PhotoStore {
    let session: NSURLSession = {
        let config = NSURLSessionConfiguration.defaultSessionConfiguration()
        return NSURLSession(configuration: config)
    }()

    func processRecentPhotosRequest(data data: NSData?, error: NSError?) -> PhotosResult {
        guard let jsonData = data else {
            return .Failure(error!)
        }
        return FlickerAPI.photosFromJSONData(jsonData)
    }

    func fetchRecentPhotos(completion completion: (PhotosResult) -> Void) {
        let url = FlickerAPI.recentPhotosURL()
        let request = NSURLRequest(URL: url)
        print("Request: \(request)")
        let task = session.dataTaskWithRequest(request) {
            (data, response, error) -> Void in

            let result = self.processRecentPhotosRequest(data: data, error: error)
            completion(result)
        }
        task.resume()
    }

    func fetchImageForPhoto(photo: Photo, completion: (ImageResult) -> Void) {

        // don't redownload image if already downloaded
        if let image = photo.image {
            completion(.Success(image))
        }

        let photoURL = photo.remoteURL
        let request = NSURLRequest(URL: photoURL)
        let task = session.dataTaskWithRequest(request) {
            (data, response, error) -> Void in
            let result = self.processImageRequest(data: data, error: error)
            if case let .Success(image) = result {
                print("image: \(image)")
                photo.image = image
            }
            print("Result: \(result)")
            if let hr = response as? NSHTTPURLResponse {
                print("Response: \(hr.statusCode), \(hr.allHeaderFields)")
            }


            completion(result)
        }
        task.resume()
    }

    func processImageRequest(data data: NSData?, error: NSError?) -> ImageResult {
        guard let imageData = data,
            image = UIImage(data: imageData) else {
                if data == nil {
                    return .Failure(error!)
                } else {
                    return .Failure(PhotoError.ImageCreationError)
                }
        }
        print (image)
        return .Success(image)
    }
}