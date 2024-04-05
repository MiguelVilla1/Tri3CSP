---
permalink: /maps
layout: base
title: maps
---
<html style="height: 100%; margin: 0; padding: 0;">
<head>
  <title>Volunteer Map</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      background-color: #E3DAC9;
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
    header {
      background-color: #E3DAC9; /* Set background color for the header */
      color: white; /* Set text color for the header */
      padding: 10px 0; /* Add padding to the header */
      text-align: center; /* Center align text within the header */
    }
  </style>
<body>
  <header>
    <h1>Volunteer Map</h1>
  </header>
  <!--The div element for the map -->
  <div id="map-container">
    <div id="map"></div>
  </div>
</body>
  <script src="https://polyfill.io/v3/polyfill.min.js?features=default"></script>
  <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC9pEqmLuhD8-W86bZHiuDpCgeXlCoxVTc&callback=initMap"
  async defer></script>
  <script type="text/javascript">
    let map;
    async function initMap() {
      map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 37.0902, lng: -95.7129}, // Centered of America
        zoom: 4, // Adjust the zoom level as needed
        styles: [] // Remove custom styles
      });
      const markers = [];  
      const options = {
          method: 'GET', // *GET, POST, PUT, DELETE, etc.
          mode: 'cors', // no-cors, *cors, same-origin
          cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
          credentials: 'include', // include, same-origin, omit
          headers: {
              'Content-Type': 'application/json',
          },
        };
        if (location.hostname === "localhost") {
        uri = "http://localhost:8965";
        } else if (location.hostname === "127.0.0.1") {
        uri = "http://127.0.0.1:8965";
        } else {
        uri = "https://oppconn.stu.nighthawkcodingsociety.com";
        }
        const url = uri + '/api/events/';
        const response = await fetch(url, options);
          if (response.status !== 200) {
            const errorMsg = 'Database response error: ' + response.status;
            console.log(errorMsg);
            return;
            }           
            const events = await response.json();  
            //const distinctAddrs = [...new Set(events.map(item => item.name))];
            const addrs = events.reduce((map, obj) => {
            if (!map.has(obj.address)) {
              map.set(obj.address, obj.title); 
            }
            return map;
            }, new Map());
          // Convert Map to an array of objects
          const distinctAddrs = Array.from(addrs, ([address, title]) => ({ address, title }));     
              for(const addr of distinctAddrs){           
              var geocoder = new google.maps.Geocoder();
              await geocoder.geocode({'address':addr.address}, function(results, status){                
                if(status === 'OK'){                  
                  var location = results[0].geometry.location;
                  let jsonObject = { lat: location.lat(), lng: location.lng(), label:addr.title };
                  markers.push(jsonObject);
                } else {
                  alert('Geocode was not successful for the following reason: ' + status);
                }
              });
            }           
          markers.forEach(marker => {
          const newMarker = new google.maps.Marker({
            position: marker,
            map: map,
            title: marker.label // Display label as marker title
          });
          // Add click event listener to the marker
          newMarker.addListener('click', function() {
            alert('Place: ' + marker.label + '\nLatitude: ' + this.getPosition().lat() + '\nLongitude: ' + this.getPosition().lng());
          });
        }); 
      }
  </script>
</head>
<body>
  <!--The div element for the map -->
  <div id="map-container">
    <div id="map"></div>
  </div>
</body>
</html>