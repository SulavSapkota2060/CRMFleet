// Array of all the questions and choices to populate the questions. This might be saved in some JSON file or a database and we would have to read the data in.

var all_questions = [{
    question_string: "What is the first thing you should learn to do?",
    choices: {
      correct: "Practice your script 50 times a day",
      wrong: ['Call the carrier to get them signed up',
        'Call the broker and negotiate load rates',
        'Go on the load board and see what kind of loads you can find']
    }
  }, {
    question_string: "What to say to the owner-operator when they answer?",
    choices: {
      correct: "Hey John",
      wrong: ["Hey Owner Operator",
      'Hey Driver',
      'Hey John, how are you today?',]
    }
  }, {
    question_string: "What questions should you ask in what order?",
    choices: {
      correct: "Looking for a load there driver, you’re in, you’re driving, is that a 48 or 53 footer",
      wrong: ['Looking for a load, you’re in, you’re driving, is that a 48 or 53 footer',
        'Looking for a load there driver, you’re driving, is that a 48 or 53 footer, you’re in',
        'Looking for a load there driver, is that a 48 or 53 footer, you’re driving, you’re in']
    }
  },
  {
    question_string: "What do you say when they're on the load board and they say ready?",
    choices: {
      correct: "I got 1,2,3,4,5,6,7,8,9,10,11,12, how many do you have?",
      wrong: ["I got 1,2,3,4,5,6, how many do you have?",
      "I got 1,2,3,4,5,6,7,8, how many do you have?",
      "I got 1,2,3,4,5,6,7,8,9,10,11,12,13,14, how many do you have?"
      ]
    }
  }
  , {
    question_string: 'When they say have None, what do you say?',
    choices: {
      correct: "Exactly, We can find high paying freight faster than anyone else on the planet",
      wrong: [" Exactly, I can’t legally do anything for you without an agreement",
      'Exactly, we specialize in only high paying freight',
      'Exactly, this is not a contract, it is not',
      ]
    }
  }
  , {
    question_string: 'What documents do you have to have ready to send to the driver?',
    choices: {
      correct: "Email, (LSA) Logistics Service Agreement and Profile Form",
      wrong: ['Load rate confirmation sheet',
        '(LSA) Logistics Service Agreement and carrier Invoicing sheet',
        'Signed (BOL) Bill of Lading']
    }
  }

  , {
    question_string: 'What is Our Motto?',
    choices: {
      correct: "When you see our Phone number on your Caller I.D. You will know without a shadow of a doubt that we have the kind of LOADS that you want. Going to the PLACES that you want to go. Paying you the kind of $$$$ MONEY $$$$ that you want to get paid!!!",
      wrong: ["Motto1",
    "Motto2",
  "Motto3"]
    }
  }
  , {
    question_string: 'What to say when they ask how much is it or does it cost?',
    choices: {
      correct: "Our fee is 10% of the load but before you say oh wow that's to high",
      wrong: [" Well, it’s only 10%",
      "It’s only 10% of the load",
      
      "Our fee is 10%"]
    }
  }
  , {
    question_string: 'They return the documents to you, what do you check?',
    choices: {
      correct: "LSA, Profile form, MC Authority, (COI) Certificate of Insurance, W-9",
      wrong: ["LSA, Profile form",
        "LSA, Profile form, MC Authority, Carrier Invoicing, (COI) Certificate of Insurance",
        "LSA, Profile form, MC Authority, (COI) Certificate of Insurance, Load Rate Confirmation"]
    }
  }
  , {
    question_string: 'How do we find drivers?',
    choices: {
      correct: "Trucker Path, Quick Transport",
      wrong: [" Direct Freight",
      "Trucker Path, Safer Watch",
      "FMCSA"]
    }
  }
  , {
    question_string: 'What is the first thing a Broker asks you for?',
    choices: {
      correct: "MC Number/ DOT Number",
      wrong: ["Carrier Packet",
      
      "LSA, Profile Form",
      "Size of their Trailer"]
    }

    
  }

  , {
    question_string: 'What are two possibilities that a broker may tell you?',
    choices: {
      correct: "Carrier Needs Carrier Packet or that carrier is good to go",
      wrong: ["Carrier Needs a Carrier Packet and (COI) Certificate of Insurance",
        "Carrier Needs a Profile Form, Carrier Packet",
        "That carrier is good to go, W-9 form"]
    } 
  }

  , {
    question_string: 'Once a broker clears a driver, what will they send you?',
    choices: {
      correct: "Load Rate Confirmation",
      wrong: [ "Carrier packet",
        "(BOL) Bill of Lading",
        "Driver/ Broker Agreement"]
    } 
  }

  , {
    question_string: 'When you receive the Load Rate Confirmation, what do you do?',
    choices: {
      correct: "READ, READ, READ before sending to your driver",
      wrong: ["Immediately send it to your driver",
        "Call your driver and go over it with them",
        "Send it back to the broker",
       ]
    } 
  }

  , {
    question_string: 'If there are any discrepancies on Load Rate Confirmation, what do you do?',
    choices: {
      correct: "Call the broker and find out why?",
      wrong: [' Call your driver',
      'Send it to your driver to approve it',
      'Call the shipper and check on the load']
    } 
  }

  , {
    question_string: 'Once the load is booked, what should you receive?',
    choices: {
      correct: "(BOL) Bill of Lading",
      wrong: ['Sign Load Rate Confirmation',
        'The directions to the shipper',
        'The appointment time to pick up the load']
    } 
  }

  , {
    question_string: 'After the load is delivered, what should you receive?',
    choices: {
      correct: " Signed (BOL) Bill of Lading",
      wrong: [ 'Load Rate Confirmation',
        '(LSA) Logistics Service Agreement',
        'Carrier Packet']
    } 
  }

  , {
    question_string: 'What should be included in your Carrier Invoicing?',
    choices: {
      correct: "Signed (BOL) Bill of Lading, Signed Load Rate Confirmation, (LSA) Logistics Service Agreement, Driver/Broker Agreement, if there is one.",
      wrong: ['How much the load paid',
        'Signed (BOL) Bill of Lading, Load Rate Confirmation',
        'Load Rate Confirmation, Carrier Packet, (BOL) Bill of Lading']
    } 
  }

  , {
    question_string: 'How do we find loads?',
    choices: {
      correct: "Load Boards",
      wrong: ['Word of mouth works best',
        
        'Quick Transport',
        'Brokers']
    } 
  }

  , {
    question_string: 'What recourse do we have if the driver refuses to pay us?',
    choices: {
      correct:  "Complaint to NCCD of the FMCSA",
      wrong: [ "Just have to write it off as a loss",
      
        "Contact the shipper",
        "Contact the broker"]
    } 
  }

  , {
    question_string: 'How do we find out if the carrier has been paid?',
    choices: {
      correct: "Call the broker 1 or 2 days after the load had has been delivered",
      wrong: ['Call the broker as soon as the load has been delivered',
        'Call the receiver',
        'Call the shipper']
    } 
  }

  , {
    question_string: 'What do we say if they say No, I am not looking for a load?',
    choices: {
      correct: "Oh, you already have one",
      wrong: ["Ok, sorry to bother you.",
      
      "Here’s my number call me next time you are looking for one.",
      "Alright, I can’t help you then."]
    } 
  }

  , {
    question_string: 'What if they say No, I am not on the load board?',
    choices: {
      correct: "Ok, no problem, where are you at?",
      wrong: [
       ' Ok, call me when you are on the load board.',
        'I got a whole bunch of loads, too bad.',
        'I see that you are on the load board.']
    } 
  }

  , {
    question_string: 'How many times do we do a follow-up?',
    choices: {
      correct: "1",
      wrong: [
        '2',
       ' 3 at most',
        'As many as it takes']
    } 
  }
  , {
    question_string: 'When they agree to have you send the agreement, what do you do?',
    choices: {
      correct: "Hit send as you’re talking to them.",
      wrong: [ 'Make note and continue making calls.',
        'Open your email and attach the documents and send.',
        
        'Send it the next day, first thing in the morning.']
    } 
  }
 
];
function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}
  // An object for a Quiz, which will contain Question objects.
  var Quiz = function(quiz_name) {
    // Private fields for an instance of a Quiz object.
    this.quiz_name = quiz_name;
    
    // This one will contain an array of Question objects in the order that the questions will be presented.
    this.questions = [];
  }
  
  // A function that you can enact on an instance of a quiz object. This function is called add_question() and takes in a Question object which it will add to the questions field.
  Quiz.prototype.add_question = function(question) {
    // Randomly choose where to add question
    var index_to_add_question = Math.floor(Math.random() * this.questions.length);
    this.questions.splice(index_to_add_question, 0, question);
  }
  
  // A function that you can enact on an instance of a quiz object. This function is called render() and takes in a variable called the container, which is the <div> that I will render the quiz in.
  Quiz.prototype.render = function(container) {
    // For when we're out of scope
    var self = this;
    
    // Hide the quiz results modal
    $('#quiz-results').hide();
    
    // Write the name of the quiz
    $('#quiz-name').text(this.quiz_name);
    
    // Create a container for questions
    var question_container = $('<div>').attr('id', 'question').insertAfter('#quiz-name');
    
    // Helper function for changing the question and updating the buttons
    function change_question() {
      self.questions[current_question_index].render(question_container);
      $('#prev-question-button').prop('disabled', current_question_index === 0);
      $('#next-question-button').prop('disabled', current_question_index === self.questions.length - 1);
     
      
      // Determine if all questions have been answered
      var all_questions_answered = true;
      for (var i = 0; i < self.questions.length; i++) {
        if (self.questions[i].user_choice_index === null) {
          all_questions_answered = false;
          break;
        }
      }
      $('#submit-button').prop('disabled', !all_questions_answered);
    }
    
    // Render the first question
    var current_question_index = 0;
    change_question();
    
    // Add listener for the previous question button
    $('#prev-question-button').click(function() {
      if (current_question_index > 0) {
        current_question_index--;
        change_question();
      }
    });
    
    // Add listener for the next question button
    $('#next-question-button').click(function() {
      if (current_question_index < self.questions.length - 1) {
        current_question_index++;
        change_question();
      }
    });
   
    // Add listener for the submit answers button
    $('#submit-button').click(function() {
      // Determine how many questions the user got right
      var score = 0;
      for (var i = 0; i < self.questions.length; i++) {
        if (self.questions[i].user_choice_index === self.questions[i].correct_choice_index) {
          score++;
        }
        


      
      }
      
     
      
      // Display the score with the appropriate message
      var percentage = (score / self.questions.length)*100;
      var message;
      if (percentage === 100) {
        message = 'Great job!'
      } else if (percentage >= 75) {
        message = 'You did alright.'
      } else if (percentage >= 50) {
        message = 'Better luck next time.'
      } else {
        message = 'Maybe you should try a little harder.'
      }
      $('#quiz-results-message').text(message);
      $('#quiz-results-score').html('You got <b>' + score + '/' + self.questions.length + '</b> questions correct.' + percentage);
      $('#Myscore').val(percentage);
      $('#quiz-results').slideDown();
      $('#submit-button').slideUp();
      $('#next-question-button').slideUp();
      $('#prev-question-button').slideUp();
      $('#quiz-retry-button').sideDown();
      
    });
    
    // Add a listener on the questions container to listen for user select changes. This is for determining whether we can submit answers or not.
    question_container.bind('user-select-change', function() {
      var all_questions_answered = true;
      for (var i = 0; i < self.questions.length; i++) {
        if (self.questions[i].user_choice_index === null) {
          all_questions_answered = false;
          break;
        }
      }
      $('#submit-button').prop('disabled', !all_questions_answered);
    });
  }
  
  // An object for a Question, which contains the question, the correct choice, and wrong choices. This block is the constructor.
  var Question = function(question_string, correct_choice, wrong_choices) {
    // Private fields for an instance of a Question object.
    this.question_string = question_string;
    this.choices = [];
    this.user_choice_index = null; // Index of the user's choice selection
    
    // Random assign the correct choice an index
    this.correct_choice_index =getRandomInt(4)
    
    // Fill in this.choices with the choices
    var number_of_choices = wrong_choices.length + 1;
    for (var i = 0; i < number_of_choices; i++) {
      if (i === this.correct_choice_index) {
        this.choices[i] = correct_choice;
      } else {
        // Randomly pick a wrong choice to put in this index
        var wrong_choice_index = Math.floor(Math.random(0, wrong_choices.length));
        this.choices[i] = wrong_choices[wrong_choice_index];
        
        // Remove the wrong choice from the wrong choice array so that we don't pick it again
        wrong_choices.splice(wrong_choice_index, 1);
      }
    }
  }
  
  // A function that you can enact on an instance of a question object. This function is called render() and takes in a variable called the container, which is the <div> that I will render the question in. This question will "return" with the score when the question has been answered.
  Question.prototype.render = function(container) {
    // For when we're out of scope
    var self = this;
    
    // Fill out the question label
    var question_string_h2;
    if (container.children('h2').length === 0) {
      question_string_h2 = $('<h2>').appendTo(container);
    } else {
      question_string_h2 = container.children('h2').first();
    }
    question_string_h2.text(this.question_string);
    
    // Clear any radio buttons and create new ones
    if (container.children('input[type=radio]').length > 0) {
      container.children('input[type=radio]').each(function() {
        var radio_button_id = $(this).attr('id');
        $(this).remove();
        container.children('label[for=' + radio_button_id + ']').remove();
      });
    }
    for (var i = 0; i < this.choices.length; i++) {
      // Create the radio button
      var choice_radio_button = $('<input>')
        .attr('id', 'choices-' + i)
        .attr('type', 'radio')
        .attr('name', 'choices')
        .attr('value', 'choices-' + i)
        .attr('checked', i === this.user_choice_index)
        .appendTo(container);
      
      // Create the label
      var choice_label = $('<label>')
        .text(this.choices[i])
        .attr('for', 'choices-' + i)
        .appendTo(container);
    }
    
    // Add a listener for the radio button to change which one the user has clicked on
    $('input[name=choices]').change(function(index) {
      var selected_radio_button_value = $('input[name=choices]:checked').val();
      
      // Change the user choice index
      self.user_choice_index = parseInt(selected_radio_button_value.substr(selected_radio_button_value.length - 1, 1));
      
      // Trigger a user-select-change
      container.trigger('user-select-change');
    });
  }
  
  // "Main method" which will create all the objects and render the Quiz.
  $(document).ready(function() {
    // Create an instance of the Quiz object
    var quiz = new Quiz('Trainee Upgrading Quiz');
    
    // Create Question objects from all_questions and add them to the Quiz object
    for (var i = 0; i < all_questions.length; i++) {
      // Create a new Question object
      var question = new Question(all_questions[i].question_string, all_questions[i].choices.correct, all_questions[i].choices.wrong);
      
      // Add the question to the instance of the Quiz object that we created previously
      quiz.add_question(question);
    }
    
    // Render the quiz
    var quiz_container = $('#quiz');
    quiz.render(quiz_container);
  });


