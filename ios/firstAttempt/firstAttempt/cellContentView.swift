//
//  cellContentView.swift
//  firstAttempt
//
//  Created by David.Qian on 4/17/15.
//  Copyright (c) 2015 David.Qian. All rights reserved.
//

import UIKit

class cellContentView: UIView {

    @IBOutlet var view: UIView!
    @IBOutlet var title: UILabel!
    @IBOutlet var priceLabel: UILabel!
    @IBOutlet var imageView: UIImageView!
    
    var item:NSDictionary!
    
    required init(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        
        NSBundle.mainBundle().loadNibNamed("cellContentView", owner: self, options: nil)
        self.addSubview(self.view)
    }
    
    required override init() {
        super.init()
        NSBundle.mainBundle().loadNibNamed("cellContentView", owner: self, options: nil)
        self.addSubview(self.view)
    }
    
    required init(itemDict: NSDictionary){
        super.init()
//        NSBundle.mainBundle().loadNibNamed("cellContentView", owner: self, options: nil)
        initView(itemDict)
        self.addSubview(self.view)
    }
    
    required override init(frame: CGRect) {
        super.init(frame: frame)
    }
    
    func initView(itemDict :NSDictionary){
        self.item = itemDict
        reload()
    }
    
    func reload(){
        if self.item != nil {
            let basicinfo = item["basicInfo"] as NSDictionary
            //            cell.textLabel?.text = basicinfo["title"] as? String
            let url = NSURL(string: basicinfo["galleryURL"] as String)
            let data = NSData(contentsOfURL: url!) //make sure your image in this url does exist, otherwise unwrap in a if let check
            //            cell.imageView?.image = UIImage(data: data!)
            let image:UIImage = UIImage(data: data!)!
            imageView = UIImageView(image: image)
            title = UILabel()
            title.text = basicinfo["title"] as? String
            priceLabel = UILabel()
            priceLabel.text = basicinfo["convertedCurrentPrice"] as? String
            self.setNeedsDisplay()
        }
    }
    
}
