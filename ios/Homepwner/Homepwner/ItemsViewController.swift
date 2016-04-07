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

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 3
    }

    override func tableView(tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat {

        switch indexPath.section {
        case 0:
            fallthrough
        case 1:
            return 60
        default:
            return 44
        }
    }

    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        switch section {
        case 0:
            return "Cheap"
        case 1:
            return "Expensive"
        case 2:
            // footer section
            return ""
        default:
            return "Unknown"
        }
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        print("tableView(_:numberOfRowsInSection:) called")

        // return count for cheap or expensive sections
        print ("Cheap: \(itemStore.cheapItems.count), Expensive: \(itemStore.expItems.count)")
        switch section {
        case 0:
            print("Returning cheap: \(itemStore.cheapItems.count)")
            return itemStore.cheapItems.count
        case 1:
            print("Returning expensive: \(itemStore.expItems.count)")
            return itemStore.expItems.count
        case 2:
            // single cell for footer section.
            return 1
        default:
            print("Unknown section - returning 0")
            return 0
        }
    }

    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        print("tableView(_:cellForRowAtIndexPath:) called")
        // get new or recycle cell
        let cell = tableView.dequeueReusableCellWithIdentifier("UITableViewCell", forIndexPath: indexPath)

        var item = Item()
        switch indexPath.section {
        case 0:
            // set text on cell with description of item at nth index, where n = row this will appear in.
            item = itemStore.cheapItems[indexPath.row]
            cell.textLabel?.font = UIFont.systemFontOfSize(20)
        case 1:
            // set text on cell with description of item at nth index, where n = row this will appear in.
            item = itemStore.expItems[indexPath.row]
            cell.textLabel?.font = UIFont.systemFontOfSize(20)
        case 2:
            cell.textLabel?.text = "No more items!"
            cell.detailTextLabel?.text = ""
            return cell
        default:
            break
        }
        cell.textLabel?.text = item.name
        cell.detailTextLabel?.text = "$\(item.valueInDollars)"
        cell.backgroundView=UIImageView(image: UIImage(named: "Image.png"))

        return cell
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        print("view ItemsView did load")
        // height of status bar
        let sbHeight = UIApplication.sharedApplication().statusBarFrame.height
        let insets = UIEdgeInsets(top: sbHeight, left: 0, bottom: 0, right: 0)
        tableView.contentInset = insets
        tableView.scrollIndicatorInsets = insets
        tableView.editing = true
    }
}