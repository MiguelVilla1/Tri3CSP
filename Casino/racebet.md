---
layout: default
title: Race Betting
permalink: /racebet
---

<html lang="en">


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Race Track</title>
    <style>
        body {
            background-image: url('images/racebetbackdrop.png');
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
            margin: 0;
            font-family: 'Arial', sans-serif;
            color: #ffffff; /* Text color */
            text-align: center;
            padding: 50px; /* Add padding to the content */
        }
        .textbox {
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid #ffffff;
            padding: 20px;
            margin: 20px;
            border-radius: 10px;
            max-width: 600px;
            margin: auto;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.2em;
            line-height: 1.5;
        }
        .race-track {
            position: relative;
            width: 100%;
            margin: 0 auto;
        }
        .car {
            position: absolute;
            bottom: 0;
            transition: left 3s linear;  /* Adjust the transition duration as needed */
        }
        #blueCar {
            left: 0;
            bottom: 15px;  /* Adjust the starting position for the blue car */
        }
        #redCar {
            left: 0;
            bottom: 95px;  /* Adjust the starting position for the red car */
        }
        button {
            margin-top: 20px;
            padding: 10px;
            font-size: 16px;
        }
    </style>



</head>
<body>
    <div class="textbox">
        <h1>Welcome to the Racetrack!</h1>
        <p>Please place your bets after clicking the `Start Race` button below!</p>       
    </div>
    <a href="https://jaydenchen17.github.io/casinosim/casinoroom" class="button">Back to Game Room</a>
    <div class="race-track">
        <img src="images/racetrack.png" alt="Race Track" width="1000" height="200">
        <img id="blueCar" class="car" src="images/blueracecar.png" alt="Blue Car" width="100">
        <img id="redCar" class="car" src="images/redracecar.png" alt="Red Car" width="100">
    </div>
    <button id="raceButton">Start Race</button>
    <audio id="raceSound" src="/racetracksound.mp3"></audio>
    <script src="racebet.js"></script>
</body>
</html>
