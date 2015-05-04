$(function() {
    var model = {
        init: function() {
            this.cats = [{
                name: "cat1",
                url: "https://lh3.ggpht.com/kixazxoJ2ufl3ACj2I85Xsy-Rfog97BM75ZiLaX02KgeYramAEqlEHqPC3rKqdQj4C1VFnXXryadFs1J9A=s0#w=640&h=496"
            }, {
                name: "cat2",
                url: "https://lh3.ggpht.com/nlI91wYNCrjjNy5f-S3CmVehIBM4cprx-JFWOztLk7vFlhYuFR6YnxcT446AvxYg4Ab7M1Fy0twaOCWYcUk=s0#w=640&h=426"
            }, {
                name: "cat3",
                url: "https://lh5.ggpht.com/LfjkdmOKkGLvCt-VuRlWGjAjXqTBrPjRsokTNKBtCh8IFPRetGaXIpTQGE2e7ZCUaG2azKNkz38KkbM_emA=s0#w=640&h=454"
            }, {
                name: "cat4",
                url: "https://lh4.ggpht.com/dUJNejPqb_qLsV1kfWcvviqc7adxsw02BSAm8YLWNklP4lI6fQCLKXd-28uKuchtjoEUpqFN0K6kkTSDHw=s0#w=588&h=640"
            }, {
                name: "cat5",
                url: "https://lh3.ggpht.com/cesD31eroFxIZ4IEeXPAJkx_8i5-haU3P9LQosGNfV-GfAPUh2bE4iw4zV6Mc9XobWOR70BQh2JAP57wZlM=s0#w=640&h=480"
            }];
            this.cats.forEach(function(cat) {
                cat.num = 0;
            });
            this.currentCat = this.cats[0];
            this.isEditable = false;
        },
        getAllCats: function() {
            return this.cats;
        }
    };

    var octopus = {
        init: function() {
            model.init();
            catListView.init();
            catDisplayView.init();
            adminView.init();
        },
        getCurrentCat : function(){
            return model.currentCat;
        },
        setCurrentCat : function(cat){
            model.currentCat = cat;
            catDisplayView.render();
            adminView.hide();
        },
        getAllCats: function() {
            return model.getAllCats();
        },
        incrementCounter: function(){
            model.currentCat.num++;
            catDisplayView.render();
        },
        adminClicked : function(){
            model.isEditable = !model.isEditable;
            if (model.isEditable){
                adminView.renderEditArea();
            }
            else{
                adminView.hide();
            }
        }
    };


    var catListView = {
        init: function() {
            catListView.render();
        },
        render: function() {
           $("#catList").html('');
            octopus.getAllCats().forEach(function(cat) {
                var elem = document.createElement('button');
                elem.name = cat.name;
                elem.textContent = cat.name;
                elem.addEventListener('click', function() {
                    octopus.setCurrentCat(cat);
                });
                $("#catList").append(elem);
            });

        },
    };

    var catDisplayView = {
        init: function() {
            $("#catImg").click(function(evt){
                octopus.incrementCounter();
            });
            catDisplayView.render();
        },
        render: function() {
            cat = octopus.getCurrentCat();
            $("#catName").html(cat.name);
            $("#catCount").html(cat.num);
            $("#catImg").attr('src',cat.url);
        }
    };

    var adminView = {
        init : function(){
            this.editArea = $('#editArea');
            this.name = $('#nameInput');
            this.url = $('#urlInput');
            this.num = $('#numInput');
            this.admin = $('#adminBtn');
            this.cancel  = $('#cancel');
            this.save = $('#save');
            this.admin.click(function(){
                octopus.adminClicked();
            });
            this.cancel.click(function(){
                adminView.renderEditArea();
            });
            this.save.click(function(){
                adminView.saveValue();
            });
            adminView.hide();
        },
        renderEditArea : function(){
            this.cat = octopus.getCurrentCat();
            this.editArea.show();
            this.name.val(cat.name);
            this.url.val(cat.url);
            this.num.val(cat.num);
        },
        hide : function(){
            this.editArea.hide();
        },
        saveValue : function(){
            this.cat.name = this.name.val();
            this.cat.url = this.url.val();
            this.cat.num = this.num.val();
            catDisplayView.render();
            adminView.hide();
        }
    };

    octopus.init();
});