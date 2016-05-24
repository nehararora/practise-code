//
//  DetailTextField.swift
//  Homepwner
//
//  Created by Nehar Arora on 5/21/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class DetailTextField: UITextField {

    override func becomeFirstResponder() -> Bool {
        super.becomeFirstResponder()

        // change borderStyle
        borderStyle = .Bezel
        return true
    }

    override func resignFirstResponder() -> Bool {
        super.resignFirstResponder()

        // change back to rounded rect
        borderStyle = .RoundedRect
        return true
    }
}
