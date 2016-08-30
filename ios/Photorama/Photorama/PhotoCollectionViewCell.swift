//
//  PhotoCollectionViewCell.swift
//  Photorama
//
//  Created by Nehar Arora on 8/29/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class PhotoCollectionViewCell: UICollectionViewCell {

    @IBOutlet var imageView: UIImageView!
    @IBOutlet var spinner: UIActivityIndicatorView!

    func updateWithImage(image: UIImage?) {
        if let imageToDisplay = image {
            spinner.stopAnimating()
            imageView.image = imageToDisplay
        } else {
            spinner.startAnimating()
            imageView.image = nil
        }
    }

    override func awakeFromNib() {
        super.awakeFromNib()
        spinner.hidesWhenStopped = true
        updateWithImage(nil)
    }

    override func prepareForReuse() {
        super.prepareForReuse()
        updateWithImage(nil)
    }

}
