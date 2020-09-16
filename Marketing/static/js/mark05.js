
var Utils = {

    toggleCheckBox: function (obj, targetId) {
        var check = obj.checked;
        //$("input[name='" + targetId + "']").prop("checked", check);
        $("input[name='" + targetId + "']").each(function (idx, ele) {
            var disabled = $(ele).prop("disabled");
            if(!disabled) {
                $(ele).prop("checked", check);
            }
        });
    },

    checkAtLeastOne: function(name){
        var arr = this.getCheckBoxValue(name);
        if(arr.length > 0) return true;
        else return false;
    },

    getCheckBoxValue: function(name){
        var arr = new Array();
        $("input[name='" + name + "']:checked").each(function (index, item) {
            arr.push($(item).val());
        });
        return arr;
    },

    getCheckBoxValueStr: function(name){
        var str = '';
        var arr = this.getCheckBoxValue(name);
        $.each(arr, function(index, val) {
            str += val;
            if(index < (arr.length-1)) str += ',';
        });
        return str;
    },

    getRadioValue: function(name){
        var val = '';
        $("input[name='" + name + "']:checked").each(function (index, item) {
            val = $(item).val();
        });
        return val;
    }

};


var Dialog = {

    submitDialog: function (id, option){
        $('#' + id).dialog({
            autoOpen: true,//如果設置為true，則默認頁面加載完畢后，就自動彈出對話框；相反則處理hidden狀態。
            bgiframe: true, //解決ie6中遮罩層蓋不住select的問題
            width: (typeof option === 'undefined' || option == null || typeof option.width === 'undefined' || option.width == null ? 600 : option.width),
            height: (typeof option === 'undefined' || option == null || typeof option.height === 'undefined' || option.height == null ? 600 : option.height),
            title: (!option || !option.title ? "Dialog Title" : option.title),
            modal: true,//這個就是遮罩效果
            resizable: true,
            position: {
                using: function(pos){
                    var w = $(window).width();
                    var h = $(window).height();
                    var topOffset = $(this).css(pos).offset().top;
                    if (topOffset = 0 || topOffset > 0) {
                        $(this).css('top', (h - this.height)/2);
                        $(this).css('left', (w - this.width)/2);
                    }
                }
            },
            buttons: [
                {
                    text: "Save",
                    class: "btn btn-success",
                    click: function() {
                        var isvalid = $(this).find("form").submit();
                    }
                },
                {
                    text: "Cancel",
                    class: "btn btn-danger",
                    click: function() {
                        $(this).dialog("close");
                    }
                }
            ],

            open: function(event, ui) {
                //var m = $(defaultMask).height($(window).height()).width($(window).width()); //使遮罩的背景覆蓋整個頁面
                //m.show();
            },

            close: function(event, ui) {

            }

        });
    },

    openDialog: function (id, option){
        $('#' + id).dialog({
            autoOpen: true,//如果設置為true，則默認頁面加載完畢后，就自動彈出對話框；相反則處理hidden狀態。
            bgiframe: true, //解決ie6中遮罩層蓋不住select的問題
            width: (typeof option === 'undefined' || option == null || typeof option.width === 'undefined' || option.width == null ? 600 : option.width),
            height: (typeof option === 'undefined' || option == null || typeof option.height === 'undefined' || option.height == null ? 650 : option.height),
            title: (!option || !option.title ? "Dialog Title" : option.title),
            modal: true,//這個就是遮罩效果
            resizable: true,
            position: (typeof option === 'undefined' || option == null ||
                        typeof option.position === 'undefined' || typeof option.position == null ||
                        typeof option.position.top === 'undefined' || typeof option.position.top == null ||
                        typeof option.position.left === 'undefined' || typeof option.position.left == null
                    ?
                {
                    using: function(pos){
                        var w = $(window).width();
                        var h = $(window).height();
                        var topOffset = $(this).css(pos).offset().top;
                        if (topOffset = 0 || topOffset > 0) {
                            $(this).css('top', (h - this.height)/2);
                            $(this).css('left', (w - this.width)/2);
                        }
                    }
                }
                    :
                {
                    using: function(pos){
                        var topOffset = $(this).css(pos).offset().top;
                        alert('topOffset: ' + topOffset);
                        if (topOffset = 0 || topOffset > 0) {
                            $(this).css('top', option.position.top);
                            $(this).css('left', option.position.left);
                        }
                    }

                }
            )
        });

    },

    confirm: function (title, msg, button){
        $.confirm({
            title: title,
            content: msg,
            draggable: true,
            type: 'orange',
            closeIcon: true,
            animation: 'scale',
            useBootstrap: true,
            buttons: button
        });
    },

    warning: function (msg){
        $.alert({
            type: 'red',
            title: 'Warning',
            closeIcon: true,
            content: msg
        });
    },

    success: function (msg){
        $.alert({
            type: 'green',
            title: 'Success',
            closeIcon: true,
            content: msg
        });
    },

    info: function (msg){
        $.alert({
            type: 'blue',
            title: 'Info',
            closeIcon: true,
            content: msg
        });
    },

    close: function (id){
        $('#' + id).dialog("close");
    }

};