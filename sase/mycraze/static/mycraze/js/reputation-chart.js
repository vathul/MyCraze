renderReputationsChart = function(list) {
	drawReputationsChart = function(divId, data, stackId) {
		new Highcharts.Chart({
			chart: {
	            type: 'spline',
	            renderTo : divId
	        },
	        title: {
	            text: 'Reputation Changes'
	        },
	        subtitle: {
	        	text: 'Stackoverflow User: ' + stackId
	        },
	        xAxis: {
	            type: 'datetime',
	            title: {
	                text: 'Date'
	            },        
	        },
	        yAxis: {
	            title: {
	                text: 'Reputation'
	            },
	            min: 0
	        },
	        scrollbar : {
				enabled : true
			},
	        plotOptions: {
	            spline: {
	                marker: {
	                    enabled: true,
	                    radius: 5
	                },
	                dataLabels: {
	                    enabled: true
	                }
	            }            
	        },
	        series: [{
	            name: 'Reputation',
	            data: data,
	            lineWidth: 3
	        }],
	        credits: {
	            enabled: false
	        }
		});
	}
	
	buildReputationsChart = function(divId, stats, stackId) {
		var data = [];
		for (j = stats.items.length - 1 ; j != 0 ; j--) {
			var datum = [];
			datum.push(stats.items[j].on_date*1000, stats.items[j].reputation_change);
			data.push(datum);
		}
		drawReputationsChart(divId, data, stackId);
	}
	
	gatherReputationsStats = function(i, stackId) {
		var divId = "reputations-graph-" + i;
		var newDiv = "<div id='" + divId + "' class='work-graph'></div>"
		$("#stack-graphs").append(newDiv);
		$.ajax({
			type : 'GET',
			url : "https://api.stackexchange.com/2.2/users/" + stackId
					+ "/reputation?site=stackoverflow",
			beforeSend : function() {
				$("#"+divId).html(imageHTML);
			},
			success : function(stats) {
				buildReputationsChart(divId, stats, stackId);
			},
			error : function(data) {
			},
			complete : function() {
			}
		});
	}
	
	for (i = 0; i < list.length; i++) {
		gatherReputationsStats(i, list[i]);
	}	
}