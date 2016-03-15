//
//  ConversionViewController.swift
//  WorldTrotter
//
//  Created by Nehar Arora on 3/14/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

let numberFormatter: NSNumberFormatter = {
    let nf = NSNumberFormatter()
    nf.numberStyle = .DecimalStyle
    nf.minimumFractionDigits = 0
    nf.maximumFractionDigits = 1
    
    return nf
} ()

class ConversionViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet var celsiusLabel: UILabel!
    @IBOutlet var textField: UITextField!
    
    var farenheitValue: Double? {
        didSet {
            updateCelsiusLabel()
        }
    }
    
    // computed celsius value
    var celsiusValue: Double? {
        if let value = farenheitValue {
            return (value - 32) * (5/9)
        } else {
            return nil
        }
    }
    
    @IBAction func fahrenheitFieldEditingChanged(textField: UITextField){
        
        if let text = textField.text, value = Double(text) {
            farenheitValue = value
        } else {
            farenheitValue = nil
        }
    }
    
    @IBAction func dismissKeyboard(sender: AnyObject){
        textField.resignFirstResponder()
    }

    func updateCelsiusLabel() {
        if let value = celsiusValue {
            celsiusLabel.text = numberFormatter.stringFromNumber(value)
        } else {
            celsiusLabel.text = "???"
        }
    }
    
    func textField(textField: UITextField,
        shouldChangeCharactersInRange range: NSRange,
        replacementString string: String) -> Bool {

            // disallow non-digit (and non-'.') characters.
            let digits = NSCharacterSet.decimalDigitCharacterSet()
            if string.rangeOfCharacterFromSet(digits) == nil && string.rangeOfString(".") == nil {
                return false
            }
            
            // don't allow multiple '.'s
            let existingTextHasDecimalSeparator = textField.text?.rangeOfString(".")
            let replacementTextHasDecimalSeparator = string.rangeOfString(".")
            if existingTextHasDecimalSeparator != nil &&
                replacementTextHasDecimalSeparator != nil {
                    return false
            } else {
                return true
            }
    }
}