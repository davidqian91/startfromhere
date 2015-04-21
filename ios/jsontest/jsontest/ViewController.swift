//
//  ViewController.swift
//  jsontest
//
//  Created by David.Qian on 4/16/15.
//  Copyright (c) 2015 David.Qian. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBAction func buttonPressed(sender: UIButton) {
        getJson()
    }
    
    func getJson(urlPath:String){
        let url: NSURL = NSURL(string: urlPath)!
        let session = NSURLSession.sharedSession()
        let task = session.dataTaskWithURL(url, completionHandler: {data, response, error -> Void in
            
            if error != nil {
                // If there is an error in the web request, print it to the console
                println(error.localizedDescription)
            }
            
            var err: NSError?
            var jsonResult = NSJSONSerialization.JSONObjectWithData(data, options: NSJSONReadingOptions.MutableContainers, error: &err) as NSDictionary
            if err != nil {
                // If there is an error parsing JSON, print it to the console
                println("JSON Error \(err!.localizedDescription)")
            }
            println(jsonResult)
        })
        task.resume()
        
    }
}

