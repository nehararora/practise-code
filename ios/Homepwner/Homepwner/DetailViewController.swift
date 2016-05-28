//
//  DetailViewController.swift
//  Homepwner
//
//  Created by Nehar Arora on 5/18/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class DetailViewController: UIViewController, UITextFieldDelegate,
    UINavigationControllerDelegate, UIImagePickerControllerDelegate {

    // MARK: - properties

    @IBOutlet var nameField: UITextField!
    @IBOutlet var serialNumberField: UITextField!
    @IBOutlet var valueField: UITextField!
    @IBOutlet var dateLabel: UILabel!
    @IBOutlet var imageView: UIImageView!

    var item: Item! {
        didSet {
            navigationItem.title = item.name
        }
    }

    var imageStore: ImageStore!

    //MARK: - formatters
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

    // MARK: - view methods
    override func viewWillAppear(animated: Bool) {
        super.viewWillAppear(animated)
        // fill in fields
        nameField.text = item.name
        serialNumberField.text = item.serialNumber
        valueField.text = numberFormatter.stringFromNumber(item.valueInDollars)

        dateLabel.text = dateFormatter.stringFromDate(item.dateCreated)
        // allow tapping date label to change
        dateLabel.userInteractionEnabled = true

        // set item image if present
        let displayImage = imageStore.imageForKey(item.itemKey)
        imageView.image = displayImage

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

    // MARK: - text delegate methods

    // dismiss keyboard by resigning first responder status for calling text field.
    func textFieldShouldReturn(textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }

    // MARK: - actions

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

    @IBAction func takePicture(sender: UIBarButtonItem) {
        print("take picture!")

        let imagePicker = UIImagePickerController()

        //allow editing
        imagePicker.allowsEditing = true

        // take picture if device has camera, if not pick from library
        if UIImagePickerController.isSourceTypeAvailable(.Camera) {
            imagePicker.sourceType = .Camera
        } else {
            imagePicker.sourceType = .PhotoLibrary
        }

        imagePicker.delegate = self

        // show image picker
        presentViewController(imagePicker, animated: true, completion: nil)
    }

    // MARK: - image picker delegate methods

    func imagePickerController(picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : AnyObject]) {
        // grab picked image
        let image = info[UIImagePickerControllerEditedImage] as! UIImage

        // store image
        imageStore.setImage(image, forKey: item.itemKey)

        // add to imageView
        imageView.image = image

        // get rid of picker
        dismissViewControllerAnimated(true, completion: nil)
    }

}
