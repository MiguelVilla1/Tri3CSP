---
layout: default
title: Roulette
permalink: /slots
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Slot Machine</title>
  <style>
    body {
      background-image: url('images/slotmachine.png');
      background-size: 60%;
      background-position: center center;
      background-attachment: fixed;
      margin: 0;
      font-family: 'Arial', sans-serif;
      color: #ffffff; /* Text color */
      text-align: center;
      padding: 50px; /* Add padding to the content */
    }
    .slot-machine {
      text-align: center;
      border: 10px solid gold; /* Golden border around the entire slot machine */
      padding: 20px; /* Add some padding */
      display: inline-block; /* Ensures the slot machine container fits its content */
      margin: auto; /* Center the slot machine horizontally */
    }
    .reel-container {
      margin-right: 20px; /* Add some space between reels */
      display: inline-block; /* Align reels horizontally */
      vertical-align: top; /* Align reels to the top */
    }
    .row-divider {
      width: 100%;
      height: 5px; /* Height of the row divider */
      background-color: gold; /* Color of the row divider */
      margin: 10px 0; /* Add some space above and below the row divider */
    }
    .reel {
      display: flex;
      flex-direction: column; /* Align symbols vertically */
      align-items: center; /* Center symbols horizontally */
      margin-bottom: 10px; /* Add some space between symbols */
    }
    .reel img {
      width: 100px; /* Adjust as needed */
      margin: 5px 0; /* Adjust as needed */
    }
    #spin-btn {
      background-color: gold;
      border: none;
      color: red;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
      border-radius: 5px;
      margin-top: 20px; /* Add some space above the button */
    }

  </style>
</head>
<body>
  <div class="slot-machine">
    <div class="reel-container">
      <div class="reel">
        <img src="images/slotcard.png" alt="Card">
        <img src="images/slotbar.png" alt="Bar">
        <img src="images/slot7.png" alt="Seven">
      </div>
    </div>
    <div class="reel-container">
      <div class="reel">
        <img src="images/slotcherry.png" alt="Cherry">
        <img src="images/slot7.png" alt="Seven">
        <img src="images/slotclover.png" alt="Clover">
        <!-- Add more images here -->
      </div>
    </div>
    <div class="reel-container">
      <div class="reel">
        <img src="images/slotclover.png" alt="Clover">
        <img src="images/slotcard.png" alt="Card">
        <img src="images/slot7.png" alt="Seven">
        <!-- Add more images here -->
      </div>
    </div>
  </div>
  <br>
  <br>
  <button id="spin-btn">Spin</button>
  <script src="slots.js"></script>
</body>
</html>

<br>
<br>
<body>
<a href="https://jaydenchen17.github.io/casinosim/casinoroom" class="button">Back to Game Room</a>
</body>
