//
//  resultViewController.swift
//  firstAttempt
//
//  Created by David.Qian on 4/16/15.
//  Copyright (c) 2015 David.Qian. All rights reserved.
//

import UIKit

extension String {
    
    func URLEncodedString() -> String? {
        var customAllowedSet =  NSCharacterSet.URLQueryAllowedCharacterSet()
        var escapedString = self.stringByAddingPercentEncodingWithAllowedCharacters(customAllowedSet)
        return escapedString
    }
    
    static func queryStringFromParameters(parameters: Dictionary<String,String>) -> String? {
        if (parameters.count == 0)
        {
            return nil
        }
        var queryString : String? = nil
        for (key, value) in parameters {
            if let encodedKey = key.URLEncodedString() {
                if let encodedValue = value.URLEncodedString() {
                    if queryString == nil
                    {
                        queryString = "?"
                    }
                    else
                    {
                        queryString! += "&"
                    }
                    queryString! += encodedKey + "=" + encodedValue
                }
            }
        }
        return queryString
    }
}

class resultViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    var minprice:String!
    var maxprice:String!
    var keyword:String!
    var sortOption:String!
    var dict:NSDictionary!
    var itemDict:NSDictionary!
    
    var itemCount:Int = 0
    
    @IBOutlet var waitIndicator: UIActivityIndicatorView!
    
    @IBOutlet var resultLabel: UILabel!
    
    @IBOutlet var tableView: UITableView!
    
    var urlPath = "http://danweisapp-env.elasticbeanstalk.com/backend.php?"
    var paras = ""
    var data = NSMutableData()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        paras += "keywords=\(keyword)"
        if !minprice.isEmpty {
            paras += "&minprice=\(minprice)"
        }
        if !maxprice.isEmpty {
            paras += "&maxprice=\(maxprice)"
        }
        if !sortOption.isEmpty {
            paras += "&sortOrder=\(sortOption)"
        }
        paras += "&pageSize=5"
        paras += "&pageNo=1"
        waitIndicator.startAnimating()
        self.requestForData(urlPath+paras.URLEncodedString()!)
//        tableView.
        
    }
    
    func requestForData(urlPath:String){
        println(urlPath)
        var url :NSURL = NSURL(string: urlPath)!
        let session = NSURLSession.sharedSession()
        let task = session.dataTaskWithURL(url, completionHandler: {data, response, error -> Void in
            
            if error != nil {
                // If there is an error in the web request, print it to the console
                println(error.localizedDescription)
                self.resultLabel.text="JSON Error"
            }
            var err: NSError?
            self.dict = NSJSONSerialization.JSONObjectWithData(data, options: NSJSONReadingOptions.MutableContainers, error: &err) as NSDictionary
            if err != nil {
                // If there is an error parsing JSON, print it to the console
                println("JSON Error \(err!.localizedDescription)")
                self.resultLabel.text="JSON Error"
            }
            //println(self.dict)
            self.parseJson(self.dict)
        })
        task.resume()
    }
    
    func parseJson(dict :NSDictionary){
        let isSuccess = dict["ack"] as String
        if isSuccess == "Failure"{
            println("Failure")
            resultLabel.text="Failure"
            return self.finish()
        }
        else if isSuccess == "No results found"{
            println("No results found")
            resultLabel.text="No results found"
            return self.finish()
        }
        else{
            println("Success")
            resultLabel.text="Results for \(keyword)"
        }
        let totalNum = dict["resultCount"] as Int
        let pageNumber = dict["pageNumber"] as Int
        let pageSize = dict["pageSize"] as Int
        let itemCount = dict["itemCount"] as Int
        self.itemCount = itemCount
        let startNo = pageSize*(pageNumber-1);
        
//        let item = dict["item0"] as NSDictionary
        
//        let cellContent:CellContent = CellContent(itemDict: item)
//        cellContent.frame = CGRectMake(50, 50, 200, 200)
//        self.view.addSubview(cellContent)
        self.finish()
    }
    
    func finish(){
        self.waitIndicator.stopAnimating()
        self.waitIndicator.hidden=true
        //repaint
        self.view.setNeedsDisplay()
        self.tableView.reloadData()
    }
    
    func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        var cell = UITableViewCell()
        if self.dict != nil{
            let count = indexPath.row
            let item = dict["item\(count)"] as NSDictionary
//            let basicinfo = item["basicInfo"] as NSDictionary
////            cell.textLabel?.text = basicinfo["title"] as? String
//            let url = NSURL(string: basicinfo["galleryURL"] as String)
//            let data = NSData(contentsOfURL: url!) //make sure your image in this url does exist, otherwise unwrap in a if let check
////            cell.imageView?.image = UIImage(data: data!)
//            let image:UIImage = UIImage(data: data!)!
//            cell.imageView?.image = image
//            cell.imageView?.frame = CGRectMake(0, 0, 50, 80)
//            cell.textLabel?.font = UIFont(name: "System", size: 5)
//            cell.textLabel?.text = basicinfo["title"] as? String
//            cell.detailTextLabel?.text = basicinfo["convertedCurrentPrice"] as? String
//            let backgroundView : UIView = UIView(frame: CGRectMake(0, 0, image.size.height, 100))
////            let itemView : UIView = UIView(frame: CGRectMake(0, 0, 100, 100))
//            let itemView = UIView()
//            itemView.addSubview(UIImageView(image: image))
//            var uiLabel:UILabel = UILabel(frame: CGRectMake(image.size.width, 0, 100, 100))
//            uiLabel.text = basicinfo["title"] as? String
//            itemView.addSubview(uiLabel)
//            cell.contentView.addSubview(itemView)
//            let shipprice = basicinfo["shippingServiceCost"] as String
            let cellContent:CellContent = CellContent(itemDict: item, controller:self)
//            cellContent.addToView(cell.contentView)
            cell.contentView.addSubview(cellContent)
            cell.contentView.userInteractionEnabled = true
            cell.contentView.bringSubviewToFront(cellContent)
//            let basicinfo = item["basicInfo"] as NSDictionary
//            //            cell.textLabel?.text = basicinfo["title"] as? String
//            let url = NSURL(string: basicinfo["galleryURL"] as String)
//            let data = NSData(contentsOfURL: url!)
//            let image:UIImage = UIImage(data: data!)!
//            var imageView:UIImageView = UIImageView(image: image)
//            imageView.frame = CGRectMake(0, 0, 70, 80)
//            var tap = UITapGestureRecognizer(target: self, action: Selector("imageTapped"))
//            imageView.addGestureRecognizer(tap)
//            imageView.userInteractionEnabled = true
//            cell.contentView.addSubview(imageView)
//            cell.contentView.userInteractionEnabled = true;
//            cell.bringSubviewToFront(imageView)
        }
        return cell
    }
    
    func tableView(tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat {
//        if indexPath.row == 0 {
//            return 30
//        }
//        else{
//            let count = indexPath.row-1
//            let item = dict["item\(count)"] as NSDictionary
//            let basicinfo = item["basicInfo"] as NSDictionary
//            let url = NSURL(string: basicinfo["galleryURL"] as String)
//            let data = NSData(contentsOfURL: url!)
//            let image:UIImage = UIImage(data: data!)!
//            return image.size.height
//        }
        return 80
    }
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        if self.dict != nil{
            if let itemCount = dict["itemCount"] as? Int {
                return itemCount
            }
        }
        return 1
    }
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "detailSegue" {
            let vc = segue.destinationViewController as DetailViewController
            vc.itemDict = self.itemDict
        }
    }
    
    func titleTapped(recognizer: UITapGestureRecognizer){
        let titleTap = recognizer as CustomGestureRecognizer
        self.itemDict = titleTap.getItemDict()
        self.performSegueWithIdentifier("detailSegue", sender: self)
    }
    
    func toDetailPage(itemDict :NSDictionary){
        self.itemDict = itemDict
        self.performSegueWithIdentifier("detailSegue", sender: self)
    }
}

