//
//  customizeCell.swift
//  firstAttempt
//
//  Created by David.Qian on 4/17/15.
//  Copyright (c) 2015 David.Qian. All rights reserved.
//

import UIKit
class CustomTableViewCell : UITableViewCell {
    @IBOutlet var backgroundImage: UIImageView?
    @IBOutlet var item: NSDictionary?
    func loadItem(#item: NSDictionary) {
        let basicinfo = item["basicInfo"] as NSDictionary
        //            cell.textLabel?.text = basicinfo["title"] as? String
        let url = NSURL(string: basicinfo["galleryURL"] as String)
        let data = NSData(contentsOfURL: url!) //make sure your image in this url does exist, otherwise unwrap in a if let check
        //            cell.imageView?.image = UIImage(data: data!)
        let image:UIImage = UIImage(data: data!)!
        let imageView : UIImageView = UIImageView(frame: CGRectMake(0, 0, 50, 80))
        imageView.image = image
        let itemView = UIView()
        itemView.addSubview(imageView)
        var uiLabel:UILabel = UILabel(frame: CGRectMake(50, 0, 200, 50))
        uiLabel.font = UIFont(name: "System", size: 10)
        uiLabel.text = basicinfo["title"] as? String
        itemView.addSubview(uiLabel)
        contentView.addSubview(itemView)
    }
}