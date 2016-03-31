//
//  ViewController.swift
//  Quiz
//
//  Created by Nehar Arora on 2/24/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet var currentQuestionLabel: UILabel!
    @IBOutlet var nextQuestionLabel: UILabel!
    @IBOutlet var answerLabel: UILabel!

    // constraint outlets for flying animation
    @IBOutlet var currentQuestionLabelCenterXConstraint: NSLayoutConstraint!
    @IBOutlet var nextQuestionsLabelCenterXConstraint: NSLayoutConstraint!
    
    let questions: [String] = ["From what is cognac made?",
                               "what is 7+7?",
                                "what is the capital of vermont?"]
    
    let answers: [String] = ["Grapes",
                            "14",
                            "Montpelier"]
    
    var currentQuestionIndex: Int = 0
    
    @IBAction func showNextQuestion(sender: AnyObject) {
        currentQuestionIndex += 1
        if currentQuestionIndex == questions.count{
            currentQuestionIndex = 0
        }
        
        let question: String = questions[currentQuestionIndex]
        nextQuestionLabel.text = question
            
        answerLabel.text = "???"
        animateLabelTransitions()
    }
    
    @IBAction func showAnswer(sender: AnyObject){
        let answer: String = answers[currentQuestionIndex]
        answerLabel.text = answer
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        currentQuestionLabel.text = questions[currentQuestionIndex]

        updateOffscreenLabel()
    }

    override func viewWillAppear(animated: Bool) {
        super.viewWillAppear(animated)
        nextQuestionLabel.alpha = 0
    }

    func animateLabelTransitions() {

        // force layout of views to take care of animated center X constraints
        view.layoutIfNeeded()
        let screenWidth = view.frame.width
        self.nextQuestionsLabelCenterXConstraint.constant = 0
        self.currentQuestionLabelCenterXConstraint.constant += screenWidth

        UIView.animateWithDuration(0.5,
                                   delay: 0,
                                   options: [.CurveEaseIn],
                                   animations: {
                                    self.currentQuestionLabel.alpha = 0
                                    self.nextQuestionLabel.alpha = 1
                                    self.view.layoutIfNeeded()
                                   },
                                   completion: { _ in
                                    swap(&self.currentQuestionLabel, &self.nextQuestionLabel)
                                    swap(&self.currentQuestionLabelCenterXConstraint, &self.nextQuestionsLabelCenterXConstraint)
                                    self.updateOffscreenLabel()
        })
    }

    func updateOffscreenLabel(){
        let screenWidth = view.frame.width
        nextQuestionsLabelCenterXConstraint.constant = -screenWidth
    }
}

