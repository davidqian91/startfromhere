//
//  CellContent.swift
//  firstAttempt
//
//  Created by David.Qian on 4/17/15.
//  Copyright (c) 2015 David.Qian. All rights reserved.
//

import UIKit

extension String {
    var floatValue: Float {
        return (self as NSString).floatValue
    }
}

class CellContent: UIView {
    var item:NSDictionary!
    var title: UILabel!
    var priceLabel: UILabel!
    var imageView: UIImageView!
    var controller: UIViewController!
    
    required init(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
    }
    
    required override init(frame: CGRect) {
        super.init(frame: frame)
    }
    
    required init(itemDict:NSDictionary, controller:UIViewController){
        super.init()
        self.item = itemDict
        self.controller = controller
        initView()
    }
    
    func initView(){
        let screenSize: CGRect = controller.view.bounds
        let fullWidth = screenSize.width
        println(screenSize.width)
        let basicinfo = item["basicInfo"] as NSDictionary
        //            cell.textLabel?.text = basicinfo["title"] as? String
        let url = NSURL(string: basicinfo["galleryURL"] as String)
        let data = NSData(contentsOfURL: url!) //make sure your image in this url does exist, otherwise unwrap in a if let check
        //            cell.imageView?.image = UIImage(data: data!)
        let image:UIImage = UIImage(data: data!)!
        imageView = UIImageView(image: image)
        imageView.frame = CGRectMake(0, 0, 70, 80)
        var tap = UITapGestureRecognizer(target: self, action: Selector("imageTapped"))
        imageView.addGestureRecognizer(tap)
        imageView.userInteractionEnabled = true
        title = UILabel()
        title.text = basicinfo["title"] as? String
        title.frame = CGRectMake(75, 0, fullWidth-80, 50)
        title.font = title.font.fontWithSize(13)
        title.numberOfLines = 0
        
        var titleTap = CustomGestureRecognizer(target: self.controller, action: Selector("titleTapped:"))
        let i :Int = 1
        titleTap.setItemDict(item)
        title.addGestureRecognizer(titleTap)
        title.userInteractionEnabled = true
        title.sizeToFit()
        priceLabel = UILabel()
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
            }
        }
        priceLabel.frame = CGRectMake(100, 65, fullWidth-80, 80)
        priceLabel.font = UIFont.boldSystemFontOfSize(12)
        priceLabel.sizeToFit()
        self.addSubview(title)
        self.addSubview(priceLabel)
        self.addSubview(imageView)
        self.userInteractionEnabled = true
        self.bringSubviewToFront(imageView)
        self.frame = CGRectMake(0, 0, fullWidth-80, 80)
    }
    
    
    func imageTapped()
    {
        let basicInfo = item["basicInfo"] as NSDictionary
        if let urlPath = basicInfo["viewItemURL"] as? String{
            if let url = NSURL(string: urlPath) {
                UIApplication.sharedApplication().openURL(url)
            }
        }
    }
    
}

class CustomGestureRecognizer:UITapGestureRecognizer {
    
    var itemDict:NSDictionary!
    
    func setItemDict(itemDict:NSDictionary){
        self.itemDict = itemDict
    }
    
    func getItemDict() -> NSDictionary{
        return self.itemDict
    }
}
