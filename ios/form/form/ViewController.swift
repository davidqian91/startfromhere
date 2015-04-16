import UIKit

class ViewController: UIViewController {

    @IBOutlet var email: UITextField!
    @IBOutlet var password: UITextField!

    @IBAction func buttonPressed(sender: UIButton) {
        self.email.resignFirstResponder()
        self.password.resignFirstResponder()
    }
    
    override func touchesBegan(touches: NSSet, withEvent event: UIEvent) {
        self.view.endEditing(true)
    }
    
    @IBOutlet var valueLabel: UILabel!
    @IBAction func valueChanged(sender: UISlider) {
        var value = lroundf(sender.value)
        valueLabel.text = "\(value)"
    }
}

