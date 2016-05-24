//
//  DetailViewController.swift
//  Homepwner
//
//  Created by Nehar Arora on 5/18/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class DetailViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet var nameField: UITextField!
    @IBOutlet var serialNumberField: UITextField!
    @IBOutlet var valueField: UITextField!
    @IBOutlet var dateLabel: UILabel!

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
        // fill in fields
        nameField.text = item.name
        serialNumberField.text = item.serialNumber
        valueField.text = numberFormatter.stringFromNumber(item.valueInDollars)
        dateLabel.text = dateFormatter.stringFromDate(item.dateCreated)
    }

    override func viewWillDisappear(animated: Bool) {
        super.viewWillDisappear(animated)

        // clear first responder
        view.endEditing(true)
        // "save" any user made changes
        item.name = nameField.text ?? "" //default to empty
        item.serialNumber = serialNumberField.text
        if let valueText = valueField.text, value = numberFormatter.numberFromString(valueText){
                item.valueInDollars = value.integerValue
        } else {
            item.valueInDollars = 0
        }
    }

    // dismiss keyboard by resigning first responder status for calling text field.
    func textFieldShouldReturn(textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }

    @IBAction func backgroundTapped(sender: AnyObject) {
        print("taaled")

        view.endEditing(true)
    }

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "SelectDate" {
            print("Seguing \(segue)")
            let dateSelectViewController = segue.destinationViewController as! DateSelectViewController
            dateSelectViewController.item = self.item
        }

    }
}
