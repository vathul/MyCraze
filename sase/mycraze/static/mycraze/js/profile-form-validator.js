$("#save-profile").submit(function() {
	var hasNoError = true;
    var $inputs = $("#save-profile :input").not(':button,:hidden');
	$inputs.each(function() {
		$(this).parent().removeClass('has-error');
		if($(this).val() == "") {
			$(this).parent().addClass('has-error');
			hasNoError = false;
		}
	});
	return hasNoError;
});