//
//  DrawView.swift
//  TouchTracker
//
//  Created by Nehar Arora on 6/4/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class DrawView: UIView, UIGestureRecognizerDelegate {

    var currentLines = [NSValue: Line]()
    var finishedLines = [Line]()
    var selectedLineIndex: Int?
    var moveRecognizer: UIPanGestureRecognizer!
    var thickness: Float = 1

    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)

        let doubleTapRecognizer = UITapGestureRecognizer(target: self, action: #selector(DrawView.doubleTap(_:)))
        doubleTapRecognizer.numberOfTapsRequired = 2
        doubleTapRecognizer.delaysTouchesBegan = true
        addGestureRecognizer(doubleTapRecognizer)

        let tapRecognizer = UITapGestureRecognizer(target: self, action: #selector(DrawView.tap(_:)))
        tapRecognizer.delaysTouchesBegan = true
        tapRecognizer.requireGestureRecognizerToFail(doubleTapRecognizer)
        addGestureRecognizer(tapRecognizer)

        let longPressRecognizer = UILongPressGestureRecognizer(target: self, action: #selector(DrawView.longPress(_:)))
        self.addGestureRecognizer(longPressRecognizer)

        moveRecognizer = UIPanGestureRecognizer(target:self, action: #selector(DrawView.moveLine(_:)))
        moveRecognizer.delegate = self
        moveRecognizer.cancelsTouchesInView = false
        self.addGestureRecognizer(moveRecognizer)
    }

    override func canBecomeFirstResponder() -> Bool {
        return true
    }


    func gestureRecognizer(gestureRecognizer: UIGestureRecognizer, shouldRecognizeSimultaneouslyWithGestureRecognizer otherGestureRecognizer: UIGestureRecognizer) -> Bool {
        return true
    }

    func deleteLine(sender: AnyObject) {
        // remove selected line
        if let index = selectedLineIndex {
            finishedLines.removeAtIndex(index)
            selectedLineIndex = nil
            self.setNeedsDisplay()
        }
    }

    func moveLine(gestureRecognizer: UIPanGestureRecognizer){
        print("Recognized Pan")

        if let index = selectedLineIndex {
            // recognized changes in position
            if gestureRecognizer.state == .Changed {

                let translation = gestureRecognizer.translationInView(self)
                // apply translation to start, end of selected line
                finishedLines[index].begin.x += translation.x
                finishedLines[index].begin.y += translation.y
                finishedLines[index].end.x += translation.x
                finishedLines[index].end.y += translation.y
                print("Velocity \(gestureRecognizer.velocityInView(self))")
                self.thickness = Float(gestureRecognizer.velocityInView(self).x)
                gestureRecognizer.setTranslation(CGPoint.zero, inView: self)
                // and redraw
                self.setNeedsDisplay()
            } else {
                return
            }
        }
    }

    func longPress(gestureRecognizer: UIGestureRecognizer) {
        print("Recognized a long press")
        // enable moveRecognizer
        moveRecognizer.enabled = true
        if gestureRecognizer.state == .Began {
            let point = gestureRecognizer.locationInView(self)
            selectedLineIndex = indexOfLineAtPoint(point)
            if selectedLineIndex != nil {
                currentLines.removeAll()
            }
        } else if gestureRecognizer.state == .Ended {
            selectedLineIndex = nil
        }
        self.setNeedsDisplay()
    }

    func tap(gestureRecognizer: UIGestureRecognizer){
        print("Recognized a tap")

        let point = gestureRecognizer.locationInView(self)
        selectedLineIndex = indexOfLineAtPoint(point)

        // get the menu controller
        let menu = UIMenuController.sharedMenuController()

        if selectedLineIndex != nil {
            // make drawView the target of menu actions
            self.becomeFirstResponder()

            //delete item
            let deleteItem = UIMenuItem(title: "Delete", action: #selector(DrawView.deleteLine(_:)))
            menu.menuItems = [deleteItem]

            // show menu
            menu.setTargetRect(CGRect(x: point.x, y: point.y, width: 2, height: 2), inView: self)
            menu.setMenuVisible(true, animated: true)
        } else {
            // if no line is selected, hide
            menu.setMenuVisible(false, animated: true)
        }
        setNeedsDisplay()
    }

    func doubleTap(gestureRecognizer: UIGestureRecognizer){
        print("Recognized double tap")

        selectedLineIndex = nil
        currentLines.removeAll()
        finishedLines.removeAll()
        setNeedsDisplay()
    }

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

        // draw old lines...
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

        if let index = selectedLineIndex {
            UIColor.greenColor().setStroke()
            let selectedLine = finishedLines[index]
            strokeLine(selectedLine)
        }
    }

    func indexOfLineAtPoint(point: CGPoint) -> Int? {
        // find a line close to the point
        for (index, line) in finishedLines.enumerate() {
            let begin = line.begin
            let end = line.end

            //check a few points on the line
            for t in CGFloat(0).stride(to: 1.0, by: 0.05) {
                let x = begin.x + ((end.x - begin.x) * t)
                let y = begin.y + ((end.y - begin.y) * t)

                // if the tapped point is within 20 points, return line
                if hypot(x - point.x, y - point.y) < 20.0 {
                    return index
                }
            }
        }

        // if nothing is close enough not selection
        return nil
    }

    // MARK: - Handle touch events
    override func touchesBegan(touches: Set<UITouch>, withEvent event: UIEvent?) {
        print(#function)
        // disable the moveRecognizer
        moveRecognizer.enabled = false

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
        moveRecognizer.enabled = false
        self.setNeedsDisplay()
    }

    override func touchesCancelled(touches: Set<UITouch>?, withEvent event: UIEvent?) {
        print(#function)
        currentLines.removeAll()
        self.setNeedsDisplay()
    }
}
