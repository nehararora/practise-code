//
//  ItemsViewController.swift
//  Homepwner
//
//  Created by Nehar Arora on 4/1/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class ItemsViewController: UITableViewController {
    var itemStore: ItemStore!

    @IBAction func addNewItem(sender: AnyObject) {
        let newItem = itemStore.createItem()
        
        if let index = itemStore.allItems.indexOf(newItem) {
            let indexPath = NSIndexPath(forRow: index, inSection: 0)
            tableView.insertRowsAtIndexPaths([indexPath], withRowAnimation: .Automatic)
        }
    }

    @IBAction func toggleEditingMode(sender: AnyObject) {
        if editing {
            sender.setTitle("Edit", forState: .Normal)
            setEditing(false, animated: true)
        } else {
            sender.setTitle("Done", forState: .Normal)
            setEditing(true, animated: true)
        }

    }

    override func tableView(tableView: UITableView, titleForDeleteConfirmationButtonForRowAtIndexPath indexPath: NSIndexPath) -> String? {
        return "Remove \(indexPath.row + 1)?"
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        print("tableView(_:numberOfRowsInSection:) called")
        switch section {
        case 0:
            return itemStore.allItems.count
        case 1:
            // footer row
            return 1
        default:
            return 0
        }

    }

    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        print("tableView(_:cellForRowAtIndexPath:) called")
        // get new or recycle cell
        let cell = tableView.dequeueReusableCellWithIdentifier("ItemCell", forIndexPath: indexPath) as! ItemCell

        // update labels to match preferred text size
        cell.updateLabels()
        if indexPath.section == 0 {
            // set text on cell with description of item at nth index, where n = row this will appear in.
            let item = itemStore.allItems[indexPath.row]
            cell.nameLabel.text = item.name
            cell.serialNumberLabel.text = item.serialNumber
            cell.valueLabel.text = "$\(item.valueInDollars)"
            if item.valueInDollars > 50 {
                cell.valueLabel.textColor = UIColor.redColor()
            } else {
                cell.valueLabel.textColor = UIColor.greenColor()
            }
        } else {
            cell.nameLabel.text = "No more items!"
            cell.serialNumberLabel.text = ""
            cell.valueLabel.text = ""

        }
        return cell
    }

    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {

        if editingStyle == .Delete {
            let item = itemStore.allItems[indexPath.row]

            // modal alert
            let title = "Delete \(item.name)"
            let message = "Are you sure you want to delete this item?"
            let ac = UIAlertController(title: title, message: message, preferredStyle: .ActionSheet)

            let cancelAction = UIAlertAction(title: "Cancel", style: .Cancel, handler: nil)
            ac.addAction(cancelAction)

            let deleteAction = UIAlertAction(title: "Delete", style: .Destructive, handler: {(action) -> Void in
                    self.itemStore.removeItem(item)
                    self.tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Automatic)
            })
            ac.addAction(deleteAction)

            presentViewController(ac, animated: true, completion: nil)
        }

    }

    override func tableView(tableView: UITableView, moveRowAtIndexPath sourceIndexPath: NSIndexPath, toIndexPath destinationIndexPath: NSIndexPath) {
        itemStore.moveItemToIndex(sourceIndexPath.row, toIndex: destinationIndexPath.row)
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        // height of status bar
        let sbHeight = UIApplication.sharedApplication().statusBarFrame.height
        let insets = UIEdgeInsets(top: sbHeight, left: 0, bottom: 0, right: 0)
        tableView.contentInset = insets
        tableView.scrollIndicatorInsets = insets
        tableView.rowHeight = 65
    }

    // override for showing a second footer section
    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 2
    }

    // make second section uneditable
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        return indexPath.section == 0 ? true: false
    }

    // retarget to within the first section on attempting move so that footer remains at bottom
    override func tableView(tableView: UITableView, targetIndexPathForMoveFromRowAtIndexPath sourceIndexPath: NSIndexPath, toProposedIndexPath proposedDestinationIndexPath: NSIndexPath) -> NSIndexPath {
        if proposedDestinationIndexPath.section == 1 {
            let indexPath = NSIndexPath(forRow: itemStore.allItems.count - 1, inSection: 0)
            print("Returning \(indexPath)")
            return indexPath
        } else {
            // index is within first section - return as is
            print("Returning \(proposedDestinationIndexPath)")
            return proposedDestinationIndexPath
        }
    }

    // adjust footer row height
    override func tableView(tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat {

        if indexPath.section != 0 {
            return 30
        } else {
            return 60
        }
    }

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "ShowItem" {

            // get the item that was tapped by the row
            if let row = tableView.indexPathForSelectedRow?.row {
                let item = itemStore.allItems[row]
                let detailViewController = segue.destinationViewController as! DetailViewController

                detailViewController.item = item
            }
        }
    }

    override func viewWillAppear(animated: Bool) {
        super.viewWillAppear(animated)

        tableView.reloadData()
    }
}
