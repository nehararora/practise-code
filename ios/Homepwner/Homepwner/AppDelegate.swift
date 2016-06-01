//
//  AppDelegate.swift
//  Homepwner
//
//  Created by Nehar Arora on 4/1/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    // create an item store
    var itemStore = ItemStore()

    func application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool {
        print("\(#function) activated")

        // print out bundle path
        print(" my path is: \(NSBundle.mainBundle().bundlePath)")
        // image store separate from meta-data store
        let imageStore = ImageStore()

        // set item and image stores on the item view controller
        let navController = window!.rootViewController as! UINavigationController
        let itemsController = navController.topViewController as! ItemsViewController
        itemsController.itemStore = itemStore
        itemsController.imageStore = imageStore

        return true
    }

    func applicationWillResignActive(application: UIApplication) {
        // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
        // Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game.
        print("\(#function) activated")
    }

    func applicationDidEnterBackground(application: UIApplication) {
        print("\(#function) activated")

        let saved = itemStore.saveChanges()
        if saved {
            print(" Saved all items")
        } else {
            print("Error saving items!")
        }

    }

    func applicationWillEnterForeground(application: UIApplication) {
        // Called as part of the transition from the background to the inactive state; here you can undo many of the changes made on entering the background.
        print("\(#function) activated")
    }

    func applicationDidBecomeActive(application: UIApplication) {
        // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
        print("\(#function) activated")
    }

    func applicationWillTerminate(application: UIApplication) {
        // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.
        print("\(#function) activated")
    }

}
