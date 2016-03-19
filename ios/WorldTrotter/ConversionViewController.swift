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
    
    var flag: Bool! = false

    let dark: UIColor! = UIColor.darkGrayColor()
    let light: UIColor! = UIColor(
    red: CGFloat((0xF5F4F1 & 0xFF0000) >> 16) / 255.0,
    green: CGFloat((0xF5F4F1 & 0x00FF00) >> 8) / 255.0,
    blue: CGFloat(0xF5F4F1 & 0x0000FF) / 255.0,
    alpha: CGFloat(1.0)
    )
    
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
    
    override func viewWillAppear(animated: Bool) {
        super.viewWillAppear(animated)
        print("Will appear")
        // TODO: check if we need to switch color
        if flag == true {
            print("switching to dark")
            view.backgroundColor = dark
            flag = false
        } else {
            print("switching to light")
            view.backgroundColor = light
            flag = true
        }
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        print("conversionController: I loads view")
        let currentLocale = NSLocale.currentLocale()
        print(currentLocale.objectForKey(NSLocaleCurrencySymbol))
        print(currentLocale.objectForKey(NSLocaleDecimalSeparator))
        print(currentLocale.objectForKey(NSLocaleCountryCode))
        print(currentLocale.objectForKey(NSLocaleCurrencyCode))
        print(currentLocale.objectForKey(NSLocaleUsesMetricSystem))
    }
}