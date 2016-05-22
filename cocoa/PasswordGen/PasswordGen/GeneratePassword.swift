//
//  GeneratePassword.swift
//  PasswordGen
//
//  Created by Nehar Arora on 5/22/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import Foundation



private let str = "0123456789abcdefghijklmnopqrstuvwxyz" +
                  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
                  "!@#$%^&*(()+_"


func generateRandomString(length: Int) -> String {
    var string = ""
    for _ in 0 ..< length {
        string.append(generateRandomCharacter())
    }
    return string
}


func generateRandomCharacter() -> Character {

    let index  = Int(arc4random_uniform(UInt32(str.characters.count)))

    let fromStart = str.startIndex
    let end = fromStart.advancedBy(index)
    return str[end]

}