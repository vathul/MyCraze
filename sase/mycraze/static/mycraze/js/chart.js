renderChart = function(i, category, answerCount, answerScore, questionCount,
		questionScore) {
	var divId = "tags-graph-" + i;
	var newDiv = "<div id='" + divId + "'></div>"
	$("#stack-graphs").append(newDiv);
	new Highcharts.Chart({
		chart : {
			type : 'column',
			renderTo : divId
		},
		title : {
			text : 'Top Tags'
		},
		xAxis : {
			categories : category,
			max : 4
		},
		yAxis : {
			min : 0,
			title : {
				text : 'Count / Score'
			}
		},
		scrollbar : {
			enabled : true
		},
		plotOptions : {
			column : {
				pointPadding : 0,
				borderWidth : 0
			}
		},
		series : [ {
			name : 'Answer Count',
			data : answerCount
		}, {
			name : 'Answer Score',
			data : answerScore
		}, {
			name : 'Question Count',
			data : questionCount
		}, {
			name : 'Question Score',
			data : questionScore
		} ]
	});
}

buildChart = function(i, stats) {
	var category = [];
	var answerCount = [];
	var answerScore = [];
	var questionCount = [];
	var questionScore = [];

	for (j = 0; j < stats.items.length; j++) {
		category.push(stats.items[j].tag_name);
		answerCount.push(stats.items[j].answer_count);
		answerScore.push(stats.items[j].answer_score);
		questionCount.push(stats.items[j].question_count);
		questionScore.push(stats.items[j].question_score);
	}
	renderChart(i, category, answerCount, answerScore, questionCount,
			questionScore);
}

gatherStats = function(i, stackId) {
	$.ajax({
		type : 'GET',
		url : "https://api.stackexchange.com/2.2/users/" + stackId
				+ "/top-tags?site=stackoverflow",
		success : function(stats) {
			buildChart(i, stats);
		},
		error : function(data) {
		},
		complete : function() {
		}
	});
}

renderTagsChart = function(list) {
	var stats;
	for (i = 0; i < list.length; i++) {
		stats = gatherStats(i, list[i]);
	}
}