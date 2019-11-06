$(document).ready(function(){
	// Reference to the chat messages area
  let $chatWindow = $("#messages");

  // Our interface to the Chat service
  let chatClient;

  // A handle to the room's chat channel
  let roomChannel;

  // The server will assign the client a random username - stored here
  let username;
	function print(infoMessage, asHtml) {
    let $msg = $('<div class="info">');
    if (asHtml) {
      $msg.html(infoMessage);
    } else {
      $msg.text(infoMessage);
    }
    $chatWindow.append($msg);
  }
  function printMessage(fromUser, message) {
    let $user = $('<span class="username">').text(fromUser + ":");
    if (fromUser === username) {
      $user.addClass("me");
    }
    let $message = $('<span class="message">').text(message);
    let $container = $('<div class="message-container">');
    $container.append($user).append($message);
    $chatWindow.append($container);
    $chatWindow.scrollTop($chatWindow[0].scrollHeight);
  }

  function sendmessage(msg){
  	$.getJSON(
    "/tokenn",  //address
    {
      message: msg
    },
    function(data) {
      print(data.messagefrompython,true);
    }
  );
  }
  let $form = $("#message-form");
  let $input = $("#message-input");
  $form.on("submit", function(e) {
    e.preventDefault();
    sendmessage($input.val());
    $input.val('');
  });


});