function init_map() {
    let map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 43.4643, lng: -80.5204},
        zoom: 13,
        mapTypeId: 'roadmap'
    });

    let input = document.getElementById('pac-input');
    let autocomplete = new google.maps.places.Autocomplete(input);

    autocomplete.bindTo('bounds', map);
    autocomplete.setFields(
        ['address_components', 'geometry', 'icon', 'name']);

    let infowindow = new google.maps.InfoWindow();
    let infowindowContent = document.getElementById('infowindow-content');
    infowindow.setContent(infowindowContent);
    let marker = new google.maps.Marker({
        map: map,
        anchorPoint: new google.maps.Point(0, -29)
    });

    autocomplete.addListener('place_changed', function () {
        infowindow.close();
        marker.setVisible(false);
        let place = autocomplete.getPlace();
        if (!place.geometry) {
            window.alert("No details available for input: '" + place.name + "'");
            return;
        }

        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);
        }
        marker.setPosition(place.geometry.location);
        marker.setVisible(true);

        let address = '';
        if (place.address_components) {
            address = [
                (place.address_components[0] && place.address_components[0].short_name || ''),
                (place.address_components[1] && place.address_components[1].short_name || ''),
                (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
        }

        infowindowContent.children['place-icon'].src = place.icon;
        infowindowContent.children['place-name'].textContent = place.name;
        infowindowContent.children['place-address'].textContent = address;
        infowindow.open(map, marker);

        document.getElementById("street_address").value = place.name;
        document.getElementById("city").value = place.address_components[2]['long_name'];
        document.getElementById("postal_code").value = place.address_components[6]["long_name"];
        document.getElementById("lat").value = place.geometry.location.lat();
        document.getElementById("lng").value = place.geometry.location.lng();
    });
}

function init_searchbar() {
    let input = document.getElementById('sublet-search');

    let autocomplete = new google.maps.places.Autocomplete(input);

    let circle = new google.maps.Circle({
        center: {lat: 43.4643, lng: -80.5204},
        radius: 10
    });

    autocomplete.setBounds(circle.getBounds());

    autocomplete.setFields(
        ['address_components', 'geometry', 'icon', 'name']);


    autocomplete.addListener('place_changed', function () {
        let place = autocomplete.getPlace();
        if (!place.geometry) {
            window.alert("No details available for input: '" + place.name + "'");
            return;
        }

        let address = '';
        if (place.address_components) {
            address = [
                (place.address_components[0] && place.address_components[0].short_name || ''),
                (place.address_components[1] && place.address_components[1].short_name || ''),
                (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
        }

        document.getElementById("search-lat").value = place.geometry.location.lat();
        document.getElementById("search-lng").value = place.geometry.location.lng();
    });
}

