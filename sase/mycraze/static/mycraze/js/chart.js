renderChart = function(category, answerCount, answerScore, questionCount,
		questionScore) {
	new Highcharts.Chart({
		chart : {
			type : 'column',
			renderTo : 'tags-graph'
		},
		title : {
			text : 'Tags, score and count'
		},
		xAxis : {
			categories : category,
			min : 8
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

	for (i = 0; i < stats.items.length; i++) {
		category.push(stats.items[i].tag_name);
		answerCount.push(stats.items[i].answer_count);
		answerScore.push(stats.items[i].answer_score);
		questionCount.push(stats.items[i].question_count);
		questionScore.push(stats.items[i].question_score);
	}
	renderChart(category, answerCount, answerScore, questionCount,
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