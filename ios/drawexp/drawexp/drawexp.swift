//
//  drawexp.swift
//  drawexp
//
//  Created by David.Qian on 4/16/15.
//  Copyright (c) 2015 David.Qian. All rights reserved.
//

import UIKit

class drawexp: UIView {

    // Only override drawRect: if you perform custom drawing.
    // An empty implementation adversely affects performance during animation.
    override func drawRect(rect: CGRect) {
        // Context is the object used for drawing
        let context = UIGraphicsGetCurrentContext()
        CGContextSetLineWidth(context, 3.0)
        CGContextSetStrokeColorWithColor(context, UIColor.redColor().CGColor)
        
        //create a payh
        CGContextMoveToPoint(context, 50, 100)
        CGContextAddLineToPoint(context, 130, 150)
        CGContextAddLineToPoint(context, 210, 100)
        CGContextAddLineToPoint(context, 130, 50)
        CGContextAddLineToPoint(context, 50, 100)
        
        //fill
        CGContextSetFillColorWithColor(context, UIColor.blueColor().CGColor)
        CGContextFillPath(context)
        
        //rect
//        CGContextMoveToPoint(context, 50, 60)
//        let rectangle = CGRectMake(50, 50, 200, 400)
//        CGContextAddRect(context, rectangle)
        //actually draw the path
        CGContextStrokePath(context)
        
    }
    
}
