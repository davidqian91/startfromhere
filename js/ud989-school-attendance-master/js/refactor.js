$(function(){
	var model = {
		init : function(){
			if (!localStorage.attendance) {
		        console.log('Creating attendance records...');
		        var getRandom = function() {
		            return (Math.random() >= 0.5);
		        };

		        this.attendance = [];
		        var names = ['Slappy the Frog', 'Lilly the Lizard', 'Paulrus the Walrus', 'Gregory the Goat', 'Adam the Anaconda'];
		        
		        for (var i = 0; i< names.length; i++){
		            var newObj = {};
		            newObj.row = i;
		            newObj.name = names[i];
		            newObj.attList = [];
		            for (var j = 0; j < 12; j++) {
		            	newObj.attList.push(getRandom());
		            }
		            this.attendance.push(newObj);
		        }

		        localStorage.attendance = JSON.stringify(this.attendance);
		    
		    } else{

		    	this.attendance = JSON.parse(localStorage.attendance);
		    
		    }
		},
		save : function(){
			localStorage.attendance = JSON.stringify(this.attendance);
		}
	};

	var octopus = {
		init : function(){
			model.init();
			view.init();
		},
		getAllStudentsAttd : function(){
			return model.attendance;
		},
		getStudentAttd : function(row){
			return model.attendance[row];
		},
		save : function(){
			model.save();
		}
	};

	var view = {
		init : function(){
			//init header
			this.header = $('thead tr');
			var th;
			for (var i = 0 ;i < 12; i++){
				th = document.createElement('th');
				th.textContent = i;
				this.header.append(th);
			}
			th = document.createElement('th');
			th.textContent = 'Days Missed-col';
			th.setAttribute('class', 'missed-col');
			this.header.append(th);

			var checkBoxClick = function(){
				var row = this.dataset.row;
				var col = this.dataset.col;
				view.students[row].attList[col] = this.checked;
				view.renderMissedDays(row);
				octopus.save();
			};

			//build table body
			var body = $('tbody');
			this.students = octopus.getAllStudentsAttd();
			this.students.forEach(function(student){
				var tr = document.createElement('tr');
				tr.setAttribute('class', 'student');
				var td = document.createElement('td');
				td.setAttribute('class', 'name-col');
				td.textContent = student.name;
				tr.appendChild(td);
				var input;
				for (var i = 0; i < 12; i++){
					td = document.createElement('td');
					td.setAttribute('class', 'attend-col');
					input = document.createElement('input');
					input.setAttribute('type','checkbox');
					input.setAttribute('data-col',i);
					input.setAttribute('data-row',student.row);
					if (student.attList[i]){
						input.setAttribute('checked', 'checked');
					}
					input.addEventListener('click', checkBoxClick);
					td.appendChild(input);
					tr.appendChild(td);
				}
				td = document.createElement('td');
				td.setAttribute('class', 'missed-col');
				td.textContent = 0;
				tr.appendChild(td);
				body.append(tr);
			});
			view.render();
		},
		renderMissedDays : function(row){
			var missedcol = $('tbody .missed-col')[row];
			var student = octopus.getStudentAttd(row);
			var count = 0;
			student.attList.forEach(function(b){
				if(!b){
					count ++;
				}
			});
			missedcol.textContent = count;
		},
		render : function(){
			for (var i = 0; i < this.students.length; i++){
				view.renderMissedDays(i);
			}
		}
	};

	octopus.init();
});