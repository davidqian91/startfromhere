//
//  ViewController.swift
//  helloworld
//
//  Created by David.Qian on 4/14/15.
//  Copyright (c) 2015 David.Qian. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet var NameLabel: UILabel!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func helloWorldAction(nameTextField: UITextField) {
        NameLabel.text = "Hello \(nameTextField.text)"
    }

}

