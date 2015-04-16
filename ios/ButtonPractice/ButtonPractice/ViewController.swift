//
//  ViewController.swift
//  ButtonPractice
//
//  Created by David.Qian on 4/15/15.
//  Copyright (c) 2015 David.Qian. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet var labelToShow: UILabel!

    @IBAction func buttonPressed(sender: UIButton) {
        let title = sender.titleForState(.Normal)!
        labelToShow.text = "You clicked the \(title) button"
    }

}

