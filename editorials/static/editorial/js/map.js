var init_event_map = function (id) {
    var eventApi = "/editorial/api/events/" + id + "/";
    $.getJSON(eventApi, {
            format: "json"
        })
        .done(function (data) {

            var mapOptions = {
                zoom: 8
            };
            var map = new google.maps.Map(document.getElementById("map-canvas_" + data.id), mapOptions);
            var point = new google.maps.LatLng(data.geo_lat, data.geo_long);

            new Marker({
                map: map,
                position: point,
                icon: {
                    path: MAP_PIN,
                    fillColor: data.color,
                    fillOpacity: 1,
                    strokeColor: '',
                    strokeWeight: 0
                },
                title: '{{mark.title}}',
                map_icon_label: '<span class="map-icon map-icon-postal-code-prefix"></span>'
            });

            map.setCenter(point);
            map.setZoom(16);
            $("#event_id_" + data.id).removeClass('map-event-zoom-effect');
        });

};


function initialize() {

    var eventApi = "/editorial/api/events/",
        mcOptions = {
            gridSize: 80,
            maxZoom: 10,
            styles: [
                {
                    url: '/static/editorial/events/maps/images/cluster_small.png',
                    textColor: '#FFFFFF',
                    width: 96,
                    height: 48,
                    anchor: [6, 40],
                    textSize: 12
                },
                {
                    url: '/static/editorial/events/maps/images/cluster_small.png',
                    textColor: '#FFFFFF',
                    width: 92,
                    height: 48,
                    anchor: [6, 36],
                    textSize: 12
                }
            ]
        };
    $.getJSON(eventApi, {
            format: "json"
        })
        .done(function (data) {
            var mapOptions = {},
                map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions),
                bounds = new google.maps.LatLngBounds(),
                markers = [],
                point,
                marker;
            $.each(data.results, function (index, event) {
                point = new google.maps.LatLng(event.geo_lat, event.geo_long);
                marker = new Marker({
                    map: map,
                    position: point,
                    icon: {
                        path: MAP_PIN,
                        fillColor: event.color,
                        fillOpacity: 1,
                        strokeColor: '',
                        strokeWeight: 0
                    },
                    title: event.title,
                    map_icon_label: '<span class="map-icon map-icon-postal-code-prefix"></span>'
                });
                bounds.extend(marker.position);
                google.maps.event.addListener(marker, 'click', function () {
                    map.setCenter(marker.getPosition());
                    map.setZoom(9);
                    $('#eventModal_' + event.id).modal('show');
                });
                google.maps.event.addListener(marker, 'mouseover', function () {
                    $("#event_id_" + event.id).addClass('map-event-zoom-effect');
                });
                google.maps.event.addListener(marker, 'mouseout', function () {
                    $("#event_id_" + event.id).removeClass('map-event-zoom-effect');
                });
                markers.push(marker);
                $('#eventModal_' + event.id).on('shown.bs.modal', function (e) {
                    init_event_map(event.id);
                });
            });

            new MarkerClusterer(map, markers, mcOptions);

            //now fit the map to the newly inclusive bounds
            map.fitBounds(bounds);
        });
};

google.maps.event.addDomListener(window, 'load', initialize);