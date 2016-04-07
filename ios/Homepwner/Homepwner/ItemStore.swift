//
//  ItemStore.swift
//  Homepwner
//
//  Created by Nehar Arora on 4/1/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class ItemStore {
    var allItems = [Item]()
    var cheapItems = [Item]()
    var expItems = [Item]()

    init(){
        for _ in 0..<5 {
            createItem()
        }
    }
    func createItem() -> Item {
        let newItem = Item(random: true)
        allItems.append(newItem)
        if newItem.valueInDollars <= 50 {
            cheapItems.append(newItem)
        } else {
            expItems.append(newItem)
        }
        return newItem
    }

}