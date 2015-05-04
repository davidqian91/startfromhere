//
//  ViewController.swift
//  firstAttempt
//
//  Created by David.Qian on 4/16/15.
//  Copyright (c) 2015 David.Qian. All rights reserved.
//

import UIKit

class ViewController: UIViewController,UIPickerViewDataSource,UIPickerViewDelegate {
    
    let sortOption = ["Best Match","Price: highest first","Price + Shipping: highest first","Price + Shipping: lowest first"]
    
    let sortOptValue = ["BestMatch","CurrentPriceHighest","PricePlusShippingHighest","PricePlusShippingLowest"]

    @IBOutlet var sortPicker: UIPickerView!
    @IBOutlet var keyword: UITextField!
    
    @IBOutlet var minprice: UITextField!
    
    @IBOutlet var maxPrice: UITextField!
    
    @IBOutlet var sortedBtn: UIButton!
    
    @IBOutlet var errorMsg: UILabel!
    
    @IBOutlet var coverView: UIView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        sortPicker.delegate = self
        sortPicker.dataSource = self
    }
    override func touchesBegan(touches: NSSet, withEvent event: UIEvent) {
        self.view.endEditing(true)
        self.coverView.hidden = true
    }

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        println("PREPARE FOR SEGUE")
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
        let vc = segue.destinationViewController as resultViewController
        vc.minprice = minprice.text
        vc.maxprice = maxPrice.text
        vc.keyword = keyword.text
        vc.sortOption = sortOptValue[0]
        for var i = 0; i < self.sortOption.count; ++i
        {
            if sortedBtn.titleLabel?.text == sortOption[i]{
                vc.sortOption = sortOptValue[i]
                break
            }
        }
    }
    
    @IBAction func searchSubmitted(sender: UIButton) {
        
    }

    @IBAction func clear(sender: UIButton) {
        
    }
    
    override func shouldPerformSegueWithIdentifier(identifier: String?, sender: AnyObject?) -> Bool {
        if identifier == "searchSegue"{
            return inputValidation()
        }
        return true
    }
    
    func inputValidation() -> Bool {
        errorMsg.text = ""
        var status:Bool = true
        var str:String = ""
        var minp:Int!
        var maxp:Int!
        var line:Int = 0
        if keyword.text == ""{
            str += "Please enter a keyword\n"
            status = false
            ++line
        }
        if (minprice.text != ""){
            minp = minprice.text.toInt()
            if (minp == nil){
                str += "Min price should be a valid number\n"
                status = false
                ++line
            }
        }
        if (maxPrice.text != ""){
            maxp = maxPrice.text.toInt()
            if (maxp == nil){
                str += "Max price should be a valid number\n"
                status = false
                ++line
            }
            else if (minp != nil){
                if (minp > maxp){
                    str += "Min Price should be less than max price"
                    status = false
                    ++line
                }
            }
        }
        errorMsg.text = str
        errorMsg.font = errorMsg.font.fontWithSize(13)
        errorMsg.sizeToFit()
        errorMsg.numberOfLines = line+1 
        return status
    }
    
    @IBAction func sortByBtn(sender: UIButton) {
        coverView.hidden = false
        sender.resignFirstResponder()
        UIView.animateWithDuration(1.0, delay: 0.0, options: UIViewAnimationOptions.CurveEaseIn, animations: {
            self.coverView.alpha = 1.0
            }, completion: nil)}
    
    //uipicker datasource
    func numberOfComponentsInPickerView(pickerView: UIPickerView) -> Int {
        return 1
    }
    func pickerView(pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return sortOption.count
    }
    
    //delegate
    func pickerView(pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String! {
        return sortOption[row]
    }
    
    func pickerView(pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        sortedBtn.setTitle(sortOption[row], forState: UIControlState.Normal)
        coverView.hidden = true
    }
    
}

