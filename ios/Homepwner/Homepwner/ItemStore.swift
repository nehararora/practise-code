//
//  ItemStore.swift
//  Homepwner
//
//  Created by Nehar Arora on 4/1/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class ItemStore {

    // MARK: - properties
    var allItems = [Item]()

    // use clousure to construct full path to item archive
    let itemArchiveURL: NSURL = {
        let documentsDirectories = NSFileManager.defaultManager().URLsForDirectory(.DocumentDirectory, inDomains: .UserDomainMask)
        let documentDirectory = documentsDirectories.first!
        return documentDirectory.URLByAppendingPathComponent("items.archive")
    }()

    // MARK: - initializors
    init() {
        // if archive exists use it
        if let archivedItems = NSKeyedUnarchiver.unarchiveObjectWithFile(itemArchiveURL.path!) as? [Item] {
            allItems += archivedItems
        }
    }

    // MARK: - Item manipulation
    func createItem() -> Item {
        let newItem = Item(random: true)
        allItems.append(newItem)
        return newItem
    }

    func removeItem(item: Item) {
        if let index = allItems.indexOf(item) {
            allItems.removeAtIndex(index)
        }
    }

    func moveItemToIndex(fromIndex: Int, toIndex: Int) {
        if fromIndex == toIndex {
            return
        }

        let movedItem = allItems[fromIndex]
        allItems.removeAtIndex(fromIndex)
        allItems.insert(movedItem, atIndex: toIndex)
    }

    // MARK: - archiving
    func saveChanges() -> Bool {
        print("Saving to \(itemArchiveURL.path)")
        return NSKeyedArchiver.archiveRootObject(allItems, toFile: itemArchiveURL.path!)
    }
}

