(function createQuestions(){
  var questions = [
    {
      "question": "What amount of people are you comfortable around?",
      "name": "people",
      "answers" : {
        "Lots of people": 5,
        "A small group": 3,
        "By myself": 1
      }
    },
    {
      "question": "How long is your attention span?",
      "name": "attention",
      "answers" : {
        "I can stay focused for a long time": 5,
        "Only for a couple of hours": 3,
        "Not long at all": 1
      }
    },
    {
      "question": "What type of characters do you like?",
      "name": "character",
      "answers" : {
        "All kinds": 5,
        "Humans": 3,
        "Robots/Aliens": 1
      }
    }
  ];
  var html = "";
  for (var i = 0; i < questions.length; i++){
    html += questions[i]["question"] + "<br>";
    for (var key in questions[i]["answers"]){
      html += '<input type="radio" name="' + questions[i]["name"] + '" value="';
      html += questions[i]["answers"][key] + '">' + key + "<br>";
    }
  }
  document.getElementById("quiz").innerHTML = html;
})();

function submitAnswer(){
  var total = 0;
  var categories = ["people","attention","character"];
  for (var x= 0; x < categories.length; x++){
    var choice = document.getElementsByName(categories[x]);
    for (var j=0; j < choice.length; j++){
      if(choice[j].checked){
        total += parseInt(choice[j].value);
      }
    }
  }
  var game;
  if (total < 5){
    game = "Hearthstone"
  } else if (total < 10){
    game = "Overwatch"
  } else {
    game = "World of Warcraft"
  }
  document.getElementById("results").innerHTML = game;
  }
