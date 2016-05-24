//
//  DateSelectViewController.swift
//  Homepwner
//
//  Created by Nehar Arora on 5/21/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class DateSelectViewController: UIViewController {

    @IBOutlet var nameField: UILabel!
    @IBOutlet var serialField: UILabel!
    @IBOutlet var valueField: UILabel!
    @IBOutlet var dateField: UIDatePicker!
    
    var item: Item! {
        didSet {
            navigationItem.title = item.name
        }
    }

    let numberFormatter: NSNumberFormatter = {
        let formatter = NSNumberFormatter()
        formatter.numberStyle = .DecimalStyle
        formatter.minimumFractionDigits = 2
        formatter.maximumFractionDigits = 2
        return formatter
    }()

    let dateFormatter: NSDateFormatter = {
        let formatter = NSDateFormatter()
        formatter.dateStyle = .MediumStyle
        formatter.timeStyle = .NoStyle
        return formatter
    }()

    override func viewWillAppear(animated: Bool) {
        super.viewWillAppear(animated)
        nameField.text = item.name
        serialField.text = item.serialNumber
        valueField.text = numberFormatter.stringFromNumber(item.valueInDollars)
    }

    override func viewWillDisappear(animated: Bool) {
        super.viewWillDisappear(animated)
        item.dateCreated = dateField.date
    }

}
