$(function () {
    $.get("get_overview_data", function (data) {
        set_proportion(data['proportion']);
    });
});

function set_proportion(data) {

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
