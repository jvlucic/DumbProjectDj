(function($) {
	$(document).ready(function() {
		
    grappelli.initDateAndTimePicker = function() {
        
        // HACK: get rid of text after DateField (hardcoded in django.admin)
        $('p.datetime').each(function() {
            var text = $(this).html();
            text = text.replace(/^\w*: /, "");
            text = text.replace(/<br>.*: /, "<br>");
            $(this).html(text);
        });
        
		var options = {
			// appendText: '(mm/dd/yyyy)',
			showOn : 'button',
			buttonImageOnly : false,
			buttonText : '',
			dateFormat : grappelli.getFormat('date'),
			showButtonPanel : true,
			showAnim : '',
			// HACK: sets the current instance to a global var.
			// needed to actually select today if the today-button is clicked.
			// see onClick handler for ".ui-datepicker-current"
			beforeShow : function(year, month, inst) {
				grappelli.datepicker_instance = this;
			}
		};
        var dateFields = $("input[class*='vDateField']:not([id*='__prefix__'])");
        dateFields.datepicker(options);
        
        if (typeof IS_POPUP != "undefined" && IS_POPUP) {
            dateFields.datepicker('disable');
        }
        
        // HACK: adds an event listener to the today button of datepicker
        // if clicked today gets selected and datepicker hides.
        // use live() because couldn't find hook after datepicker generates it's complete dom.
        $(".ui-datepicker-current").live('click', function() {
            $.datepicker._selectDate(grappelli.datepicker_instance);
            grappelli.datepicker_instance = null;
        });
        
        // init timepicker
        $("input[class*='vTimeField']:not([id*='__prefix__'])").grp_timepicker();

        // now-button for both date and time
        // $("<button class='ui-datetime-now' />").insertAfter("button.ui-timepicker-trigger");
        // $(".ui-datetime-now").live('click', function() {
        //     alert("Now for date and time: grappelli.js line 68 ff.");
        //     return false
        // });
    }
    grappelli.initDateAndTimePicker();
	})
})(grp.jQuery);