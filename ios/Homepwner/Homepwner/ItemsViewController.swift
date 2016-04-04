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

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        print("tableView(_:numberOfRowsInSection:) called")
        return itemStore.allItems.count
    }

    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        print("tableView(_:cellForRowAtIndexPath:) called")
        // get new or recycle cell
        let cell = tableView.dequeueReusableCellWithIdentifier("UITableViewCell", forIndexPath: indexPath)

        // set text on cell with description of item at nth index, where n = row this will appear in.
        let item = itemStore.allItems[indexPath.row]
        cell.textLabel?.text = item.name
        cell.detailTextLabel?.text = "$\(item.valueInDollars)"
        return cell
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        // height of status bar
        let sbHeight = UIApplication.sharedApplication().statusBarFrame.height
        let insets = UIEdgeInsets(top: sbHeight, left: 0, bottom: 0, right: 0)
        tableView.contentInset = insets
        tableView.scrollIndicatorInsets = insets
    }
}