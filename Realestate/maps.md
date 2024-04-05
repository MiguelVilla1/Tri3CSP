Real Estate Map
---
permalink: /maps
title: Maps
---

<html style="height: 100%; margin: 0; padding: 0;">
<head>
  <title>Real Estate Map</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      background-color: #007bff;
    }
    #map-container {
      height: 80vh; /* Adjust height as needed */
      width: 80%; /* Adjust width as needed */
      margin: 20px auto; /* Center the map horizontally */
      border: 2px solid #ccc; /* Add border */
      border-radius: 10px; /* Optional: Add border radius */
    }
    #map {
      height: 100%;
      width: 100%;
    }
  </style>
</head>
<body>
  <!--The div element for the map -->
  <div id="map-container">
    <div id="map"></div>
  </div>

  <script type="module">
    let map;

    async function initMap() {
        map = new google.maps.Map(document.getElementById("map"), {
            center: { lat: 33.000, lng: -117.200 }, // Centered at Southern California
            zoom: 8, // Adjust the zoom level as needed
            styles: [] // Remove custom styles
        });

        try {
            const favorites = await fetchFavorites();
            favorites.forEach(marker => {
                const newMarker = new google.maps.Marker({
                    position: { lat: marker.latitude, lng: marker.longitude },
                    map: map,
                    title: marker.label
                });

                newMarker.addListener('click', function() {
                    alert('Place: ' + marker.label + '\nLatitude: ' + this.getPosition().lat() + '\nLongitude: ' + this.getPosition().lng());
                });
            });
        } catch (error) {
            console.error('Error fetching favorites:', error);
        }
    }

    document.addEventListener('DOMContentLoaded', initMap);

    var uri;
    if (location.hostname === "localhost") {
        uri = "http://localhost:8181";
    } else if (location.hostname === "127.0.0.1") {
        uri = "http://127.0.0.1:8181";
    } else {
        uri = "https://rebackend.stu.nighthawkcodingsociety.com";
    }

    function getJwtToken() {
        return getCookie('jwt');
    }

    function parseJwt(token) {
        if (!token) return null;
        var base64Url = token.split('.')[1];
        var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));

        return JSON.parse(jsonPayload);
    }

    async function fetchFavorites() {
        const jwtToken = getJwtToken();
        if (!jwtToken) {
            console.error('JWT token not found.');
            return []; // Return empty array if JWT token not found
        }

        try {
            const userId = parseJwt(jwtToken).id;
            const url = uri + '/api/house/getfavorites?id=' + userId;
            const response = await fetch(url);
            if (!response.ok) throw new Error('Failed to fetch favorites.');
            const favorites = await response.json();
            return favorites;
        } catch (error) {
            throw error;
        }
    }

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
  </script>

  <script defer src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"></script>
</body>
</html>

