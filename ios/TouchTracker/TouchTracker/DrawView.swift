//
//  DrawView.swift
//  TouchTracker
//
//  Created by Nehar Arora on 6/4/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class DrawView: UIView {

    var currentLines = [NSValue: Line]()
    var finishedLines = [Line]()

    @IBInspectable var finishedLineColor: UIColor = UIColor.blackColor() {
        didSet{
            self.setNeedsDisplay()
        }
    }

    @IBInspectable var currentLineColor: UIColor = UIColor.redColor() {
        didSet {
            self.setNeedsDisplay()
        }
    }

    @IBInspectable var lineThickness: CGFloat = 10 {
        didSet {
            self.setNeedsDisplay()
        }
    }

    // MARK: - Drawing

    func strokeLine(line: Line) {

        let path = UIBezierPath()

        path.lineWidth = self.lineThickness
        path.lineCapStyle = CGLineCap.Round

        path.moveToPoint(line.begin)
        path.addLineToPoint(line.end)
        path.stroke()
    }

    override func drawRect(rect: CGRect) {

        // draw lines old lines...
        self.finishedLineColor.setStroke()

        for line in finishedLines {
            let angle = atan2(line.end.y - line.begin.y,
                              line.end.x - line.begin.x)

            UIColor(hue: abs(angle), saturation: 1, brightness: 1, alpha: 1).setStroke()
            strokeLine(line)
        }

        // draw current line
        //self.currentLineColor.setStroke()

        for (_, line) in currentLines {
            let angle = atan2(line.end.y - line.begin.y,
                              line.end.x - line.begin.x)

            print("Angle of line: \(angle)")
            UIColor(hue: abs(angle), saturation: 1, brightness: 1, alpha: 1).setStroke()
            strokeLine(line)
        }
    }

    // MARK: - Handle touch events
    override func touchesBegan(touches: Set<UITouch>, withEvent event: UIEvent?) {
        print(#function)

        for touch in touches {
            let location = touch.locationInView(self)
            let newLine = Line(begin: location, end: location)
            let key = NSValue(nonretainedObject: touch)
            currentLines[key] = newLine
        }
        setNeedsDisplay()
    }

    override func touchesMoved(touches: Set<UITouch>, withEvent event: UIEvent?) {
        print(#function)

        for touch in touches {
            let key = NSValue(nonretainedObject: touch)
            currentLines[key]?.end = touch.locationInView(self)
        }

        self.setNeedsDisplay()
    }

    override func touchesEnded(touches: Set<UITouch>, withEvent event: UIEvent?) {
        print(#function)

        for touch in touches {
            let key = NSValue(nonretainedObject: touch)
            if var line = currentLines[key] {
                line.end = touch.locationInView(self)
                finishedLines.append(line)
                currentLines.removeValueForKey(key)
            }
        }
        self.setNeedsDisplay()
    }

    override func touchesCancelled(touches: Set<UITouch>?, withEvent event: UIEvent?) {
        print(#function)
        currentLines.removeAll()
        self.setNeedsDisplay()
    }
}
