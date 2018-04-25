

$(function () {
    $.get("get_overview_data", function (data) {
        set_proportion(data['proportion']);
        set_line_charts(data['line_data']);
        set_bar_charts(data['bar_data']);
        set_area_charts(data['area_data'])
    }, 'json');
});


function set_proportion(data) {
    if (data){
        $('#h1').text(data[0]['name']);
        $('#easypiechart-blue').data('easyPieChart').update(data[0]['proportion']);
        $('#easypiechart-blue').find('span').text(data[0]['proportion'] + '%');
        $('#h2').text(data[1]['name']);
        $('#easypiechart-orange').data('easyPieChart').update(data[1]['proportion']);
        $('#easypiechart-orange').find('span').text(data[1]['proportion'] + '%');
        $('#h3').text(data[2]['name']);
        $('#easypiechart-teal').data('easyPieChart').update(data[2]['proportion']);
        $('#easypiechart-teal').find('span').text(data[2]['proportion'] + '%');
        $('#h4').text(data[3]['name']);
        $('#easypiechart-red').data('easyPieChart').update(data[3]['proportion']);
        $('#easypiechart-red').find('span').text(data[3]['proportion'] + '%');
    }

}

function set_line_charts(data) {
    var line_chart = echarts.init(document.getElementById('echarts-line-chart'));
    var option = {
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:['金额']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: data['year']
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name:'金额',
                type:'line',
                stack: '总量',
                data:data['data'],
                smooth: true
            }
        ]
    };

    line_chart.setOption(option);
}

function set_bar_charts(data) {
    var bar_charts = echarts.init(document.getElementById('echarts-bar-chart'));
    var option = {
        legend: {
            data:['年最高消费']
        },
        color: ['#0fc79a'],
        tooltip : {
            trigger: 'axis',
            axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis : [
            {
                type : 'category',
                data : data['year'],
                axisTick: {
                    alignWithLabel: true
                }
            }
        ],
        yAxis : [
            {
                type : 'value'
            }
        ],
        series : [
            {
                name:'年最高消费',
                type:'bar',
                barWidth: '60%',
                data:data['data']
            }
        ]
    };

    bar_charts.setOption(option);
}

function set_area_charts(data) {

}

var date = new Date();

$('#year').val(date.getFullYear());

$('#year').bind('keyup', function () {
    var year = $('#year').val();
    check_year(year);
    if (event.keyCode == "13"){
        reload_area_chart(year);
    }
});

$('#prev').on('click', function () {
    var year = $('#year').val();
    $('#year').val(Number(year) - 1);
    check_year($('#year').val());

});

$('#next').on('click', function () {
    var year = $('#year').val();
    year  = Number(year) + 1;
    check_year(year);
});

function check_year(year) {
    if (year.length > 4 || year > date.getFullYear() || year < 1975){
        $('#year').val(date.getFullYear());
        return;
    }
    $('#year').val(year);
    reload_area_chart(year);
}

function reload_area_chart(year) {
    $.ajax({
        url: 'reload_area_charts',
        dataType: 'json',
        type: 'GET',
        data: {'year': year},
        success: function (data) {
            if (data){
                set_area_charts(year);
            }
        }
    });
}