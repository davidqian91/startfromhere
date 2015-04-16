import UIKit

class ViewController: UIViewController, UITableViewDataSource {
    
    let people = [
        ("Alice","LA"),
        ("Bob","SF"),
        ("Ema","NY")
    ]
    
    let game = [
        ("hs","blizzard"),
        ("wow","blizzard"),
        ("cs","valve"),
        ("dota","valve")
    ]
    
    func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 2
    }
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        if section == 0 {
            return people.count
        }
        else{
            return game.count
        }
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        var cell = UITableViewCell()
        if indexPath.section == 0 {
            let (peopleName,city) = people[indexPath.row]
            cell.textLabel?.text = peopleName
        }
        else{
            let (gameName,company) = game[indexPath.row]
            cell.textLabel?.text = gameName
        }
        return cell
    }
    
    func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        if section == 0{
            return "People"
        }
        else{
            return "Game"
        }
    }
    
}

