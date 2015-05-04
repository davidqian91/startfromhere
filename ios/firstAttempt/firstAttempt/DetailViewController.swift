//
//  DetailViewController.swift
//  firstAttempt
//
//  Created by David.Qian on 4/18/15.
//  Copyright (c) 2015 David.Qian. All rights reserved.
//

import UIKit

class DetailViewController: UIViewController, UITableViewDataSource, FBSDKSharingDelegate{
    
    let labelTitles = [["CategoryName","Condition","Buying Format"],
        ["User Name", "Feedback Score", "Positive Feedback", "Feedback Rating", "Top Rated","Store"],
        ["Shipping Type","Handling Time", "Shipping Locations", "Expedited Shipping","One Day Shipping","Returns Accepted"]]
    var tabIndex:Int = 0
    var itemDict:NSDictionary!
    var shareDescription:String = ""
    
    @IBOutlet var imageView: UIImageView!
    
    @IBOutlet var titleLabel: UILabel!
    @IBOutlet var priceLabel: UILabel!
    @IBOutlet var locationLabel: UILabel!
    @IBOutlet var topRated: UIImageView!
    @IBOutlet var table: UITableView!
    var fbLoginManager: FBSDKLoginManager!
    
    @IBAction func seller(sender: UIButton) {
        if tabIndex != 1{
            self.tabIndex = 1
            table.reloadData()
        }
    }
    
    @IBAction func shipping(sender: UIButton) {
        if tabIndex != 2{
            self.tabIndex = 2
            table.reloadData()
        }
    }
    @IBAction func basicInfo(sender: UIButton) {
        if tabIndex != 0{
            self.tabIndex = 0
            table.reloadData()
        }
    }
    
    
    @IBAction func buyItNow(sender: AnyObject) {
        let basicInfo = itemDict["basicInfo"] as NSDictionary
        if let urlPath = basicInfo["viewItemURL"] as? String{
            if let url = NSURL(string: urlPath) {
                UIApplication.sharedApplication().openURL(url)
            }
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        if itemDict != nil {
            //fb login manager
            self.fbLoginManager = FBSDKLoginManager()
            fbLoginManager.loginBehavior = FBSDKLoginBehavior.SystemAccount
            
            let basicinfo = itemDict["basicInfo"] as NSDictionary
            let url = NSURL(string: basicinfo["galleryURL"] as String)
            let data = NSData(contentsOfURL: url!)
            let image:UIImage = UIImage(data: data!)!
            imageView.image = image
            titleLabel.text  = basicinfo["title"] as? String
            titleLabel.numberOfLines = 0
            titleLabel.font = titleLabel.font.fontWithSize(15)
            titleLabel.sizeToFit()
            if let price:String = basicinfo["convertedCurrentPrice"] as? String{
                if let shippingprice = basicinfo["shippingServiceCost"] as? NSString {
                    let shipPriceF = shippingprice.floatValue
                    var shipText:String!
                    if shipPriceF == 0.0 {
                        shipText = "(Free Shipping)"
                    }
                    else{
                        shipText = "(+$\(shipPriceF) Shipping)"
                    }
                    priceLabel.text = "Price: $\(price) \(shipText)"
                    shareDescription = "Price: $\(price) \(shipText)"
                    priceLabel.font = priceLabel.font.fontWithSize(12)
                    if let locationStr = basicinfo["location"] as? String{
                        locationLabel.text  = locationStr
                        locationLabel.font = locationLabel.font.fontWithSize(12)
                        self.shareDescription += " Location: "
                        self.shareDescription += locationStr
                    }
                }
            }
            
            
            if basicinfo["topRatedListing"] as String == "true"{
                topRated.hidden = false
            }
            else{
                topRated.hidden = true
            }
            table.reloadData()
        }
    }
    
    func createLabel(title:String) ->UILabel{
        let label = UILabel(frame: CGRectMake(0, 0, 100, 50))
        label.text = title
        return label
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return labelTitles[tabIndex].count
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = UITableViewCell()
        let title:String = labelTitles[tabIndex][indexPath.row]
        let titleLabel =  UILabel(frame: CGRectMake(20, 0, 150, 50))
        titleLabel.font = titleLabel.font.fontWithSize(12)
        titleLabel.text = title
        let infoLabel:UIView = buildInfoLabel(self.tabIndex, row: indexPath.row)
        cell.contentView.addSubview(titleLabel)
        cell.contentView.addSubview(infoLabel)
        return cell
    }
    
    func buildInfoLabel(index:Int, row:Int) ->UIView{
        switch index{
        case 0: return buildBasicInfoLabel(row)
        case 1: return buildSellerLabel(row)
        case 2: return buildShippingLabel(row)
        default: return UILabel()
        }
    }
    
    func buildBasicInfoLabel(row:Int) -> UILabel{
        var text:String!
        let basicInfo = itemDict["basicInfo"] as NSDictionary
        switch row{
        case 0: text = basicInfo["categoryName"] as String
        case 1: text = basicInfo["conditionDisplayName"] as String
        case 2: text = basicInfo["listingType"] as String
        if (text=="AuctionWithBIN"){
            text="Buy It Now"
            }
        default: return UILabel()
        }
        var label = UILabel(frame: CGRectMake(150, 0, 320, 50))
        label.font = label.font.fontWithSize(12)
        label.text = text
        return label
    }
    
    func buildSellerLabel(row:Int) -> UIView{
        var text:String!
        let sellerInfo = itemDict["sellerInfo"] as NSDictionary
        switch row{
        case 0: text = sellerInfo["sellerUserName"] as String
        case 1: text = sellerInfo["feedbackScore"] as String
        case 2: text = sellerInfo["positiveFeedbackPercent"] as String
        case 3: text = sellerInfo["feedbackRatingStar"] as String
        case 4: text = sellerInfo["topRatedSeller"] as String
        case 5: text = sellerInfo["sellerStoreName"] as String
        default: return UILabel()
        }
        if text == ""{
            text = "N/A"
        }
        else if text == "true"{
            var image = UIImageView(image: UIImage(named: "check"))
            image.frame = CGRectMake(150, 15, 18, 18)
            return image
        }
        else if text == "false"{
            var image = UIImageView(image: UIImage(named: "cross"))
            image.frame = CGRectMake(150, 15, 18, 18)
            return image
        }
        var label = UILabel(frame: CGRectMake(150, 0, 150, 50))
        label.font = label.font.fontWithSize(12)
        label.text = text
        return label
    }
    
    func buildShippingLabel(row:Int) -> UIView{
        var text:String!
        var flag:Int!
        let shipInfo = itemDict["shippingInfo"] as NSDictionary
        switch row{
        case 0: text = shipInfo["shippingType"] as String
        case 1: text = shipInfo["handlingTime"] as String
        case 2: text = shipInfo["shipToLocations"] as String
        case 3: flag = shipInfo["expeditedShipping"] as Int
        case 4: flag = shipInfo["oneDayShippingAvailable"] as Int
        case 5: flag = shipInfo["returnsAccepted"] as Int
        default: return UILabel()
        }
        if row < 3{
            var label = UILabel(frame: CGRectMake(150, 0, 150, 50))
            label.font = label.font.fontWithSize(12)
            label.text = text
            return label
        }
        else{
            var name:String!
            if flag == 1 {
                name = "check"
            }
            else{
                name = "cross"
            }
            var image = UIImageView(image: UIImage(named: name))
            image.frame = CGRectMake(150, 15, 18, 18)
            return image
            
        }
    }
    
    //facebook
    @IBAction func fbPressed(sender: UIButton) {
        if (FBSDKAccessToken.currentAccessToken() != nil){
            println("already login")
            let basicInfo = itemDict["basicInfo"] as NSDictionary
            let content : FBSDKShareLinkContent = FBSDKShareLinkContent()
            content.contentURL = NSURL(string: basicInfo["viewItemURL"] as String)
            content.contentTitle = basicInfo["title"] as String
            content.contentDescription = self.shareDescription
            content.imageURL = NSURL(string: basicInfo["galleryURL"] as String)
            FBSDKShareDialog.showFromViewController(self, withContent: content, delegate: self)
        }
        else{
            self.fbLoginManager.logInWithPublishPermissions(["publish_actions"], handler: { (result: FBSDKLoginManagerLoginResult!, error: NSError!) -> Void in
                print(result.token)
                if (error != nil){
                    println(error)
                }
                if result.grantedPermissions.containsObject("publish_actions"){
                    println("longin success")
                }
            })
        }
        //        if (FBSDKAccessToken.currentAccessToken() != nil)
        //        {
        //            // User is already logged in, do work such as go to next view controller.
        //        }
        //        else
        //        {
        //            let loginView : FBSDKLoginButton = FBSDKLoginButton()
        //            self.view.addSubview(loginView)
        //            loginView.center = self.view.center
        //            loginView.readPermissions = ["public_profile", "email", "user_friends"]
        //            loginView.delegate = self
        //        }
        
    }
    
    func sharer(sharer: FBSDKSharing!, didCompleteWithResults results: [NSObject : AnyObject]!) {
        let res:NSDictionary = results as NSDictionary
        if res.count == 0{
            println("cancel")
            var alert = UIAlertController(title: "Facebook Sharing Result", message: "User Cancelled", preferredStyle: UIAlertControllerStyle.Alert)
            alert.addAction(UIAlertAction(title: "Confirm", style: UIAlertActionStyle.Default, handler: nil))
            self.presentViewController(alert, animated: true, completion: nil)
        }
        else{
            let postId:String = res.valueForKey("postId") as String
            println("success, postId: \(postId)")
            var alert = UIAlertController(title: "Facebook Sharing Result", message: "Success\nPostId: \(postId)", preferredStyle: UIAlertControllerStyle.Alert)
            alert.addAction(UIAlertAction(title: "Confirm", style: UIAlertActionStyle.Default, handler: nil))
            self.presentViewController(alert, animated: true, completion: nil)
        }
    }
    
    func sharer(sharer: FBSDKSharing!, didFailWithError error: NSError!) {
        println("error")
    }
    
    func sharerDidCancel(sharer: FBSDKSharing!) {
        println("cancel")
    }
}
