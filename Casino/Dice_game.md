---
layout: default
title: Roulette
permalink: /Dice_game
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dice Game</title>
    <style>
        body {
            background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBRYqhGagTiAsOCi1B5Wjs1sjMUr6prtPTkI0h2RP4S19l2Kyh7JrzCYKOcqAxD6WnEpg&usqp=CAU');
            background-size: cover;
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        h1, p {
            color: white;
            text-shadow: 2px 2px 2px black;
        }
        .button {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 10px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 18px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
            transition-duration: 0.4s;
        }
        .button:hover {
            background-color: #45a049;
        }
        #balance {
            background-color: white;
            color: black;
            padding: 15px;
            border-radius: 12px;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <h1>Dice Game</h1>
    <p>Roll the dice and see if you win!</p>
    <div id="balance">$150</div>
    <button class="button" onclick="startGame()">Start Game</button>
    <script>
        var balance = 150;
        function startGame() {
            var betAmount = getBetAmount();
            if (!isValidBet(betAmount)) return;
            var diceNumber = getDiceNumber();
            if (!isValidDiceNumber(diceNumber)) return;
            var diceResult = rollDice();
            var resultMessage = getResultMessage(diceResult, diceNumber, betAmount);
            updateBalance(resultMessage, betAmount);
            alert(resultMessage);
        }
        function getBetAmount() {
            return parseInt(prompt("Enter your bet amount (current balance: $" + balance + "):"));
        }
        function isValidBet(betAmount) {
            if (isNaN(betAmount) || betAmount <= 0 || betAmount > balance) {
                alert("Invalid bet amount. Please enter a valid amount.");
                return false;
            }
            return true;
        }
        function getDiceNumber() {
            return parseInt(prompt("Enter the dice number you want to bet on (1-6):"));
        }
        function isValidDiceNumber(diceNumber) {
            if (isNaN(diceNumber) || diceNumber < 1 || diceNumber > 6) {
                alert("Invalid dice number. Please enter a number between 1 and 6.");
                return false;
            }
            return true;
        }
        function rollDice() {
            return Math.floor(Math.random() * 6) + 1;
        }
        function getResultMessage(diceResult, diceNumber, betAmount) {
            var message = "You rolled a " + diceResult + ". ";
            if (diceResult === diceNumber) {
                message += "Congratulations! You win $" + (betAmount * 2) + "!";
            } else {
                message += "Sorry, you lose $" + betAmount + ".";
            }
            return message;
        }
        function updateBalance(resultMessage, betAmount) {
            if (resultMessage.includes("Congratulations")) {
                balance += betAmount;
            } else {
                balance -= betAmount;
            }
            document.getElementById('balance').innerText = "$" + balance;
        }
    </script>
    <a href="https://jaydenchen17.github.io/casinosim/casinoroom" class="button">Back to Game Room</a>
</body>
</html>
