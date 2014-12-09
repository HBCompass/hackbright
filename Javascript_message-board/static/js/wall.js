$(document).ready(function () {
    // Normally, JavaScript runs code at the time that the <script>
    // tags loads the JS. By putting this inside a jQuery $(document).ready()
    // function, this code only gets run when the document finishing loading.

    getMessages();
    $("#message-form").submit(handleFormSubmit);
    $('#message-clear').click(clearMessages);
});


/**
 * Handle submission of the form.
 */
function handleFormSubmit(evt) {
    evt.preventDefault();

    var textArea = $("#message"); //identify the css-selector
    // console.log("textareaobj:", textArea);
    var msg = textArea.val(); //evaluate the selector to get its value
    // console.log("message:", msg);
    
    try {
        msg = $(msg)[0].textContent; //take the value obj and grab the text content
    }
    catch (e) {
        console.log("Sad face!", e);
    }

    addMessage(msg);
    // Reset the message container to be empty
    textArea.val("");

    var btn = $('#message-send');
    btn.prop('disabled', true);
    window.setTimeout(function() {
        btn.prop('disabled', false);
    }, 5000);
}

function clearMessages(evt){
    $.post(
        "/api/wall/delete",
        function(data) {
            getMessages();
        }
        );
}


/**
 * Makes AJAX call to the server, returns all messages.
 */
function getMessages() {
    $.get(
        "/api/wall/list",
        function (data) {
            //clear the message container
            $('#message-container').empty();
            // console.log(data);
            for (var m in data['messages']){ //loop through the arrays within data['messages']
                // console.log("m:", m);
                // console.log("m[message]:", data['messages'][m]['message']); // confirm that the message is correct
                // var entry = "<li class='list-group-item'>" + data['messages'][m]['message'] + "</li>";
                var entry = "<li class='list-group-item'>" + data.messages[m].message + "</li>";

                $('#message-container').prepend(entry);}
        }
        );
}

/**
 * Makes AJAX call to the server and the message to it.
 */
function addMessage(msg) {
    $.post(
        "/api/wall/add",
        {'m': msg},
        function (data) {
            // console.log("addMessage: ", data);
            // console.log("data.result:", data.result);
            displayResultStatus(data.result);
            getMessages();
        }
    );
}


/**
 * This is a helper function that does nothing but show a section of the
 * site (the message result) and then hide it a moment later.
 */
function displayResultStatus(resultMsg) {
    var notificationArea = $("#sent-result");

    var alertclass = "alert alert-success";
    if (resultMsg == "Your message is empty") {
        alertclass = "alert alert-warning";
    }

    notificationArea.removeClass();
    notificationArea.addClass(alertclass);

    notificationArea.text(resultMsg);
    notificationArea.slideDown(function () {
        // In JavaScript, "this" is a keyword that means "the object this
        // method or function is called on"; it is analogous to Python's
        // "self". In our case, "this" is the #sent-results element, which
        // is what slideDown was called on.
        //
        // However, when setTimeout is called, it won't be called on that
        // same #sent-results element--"this", for it, wouldn't be that
        // element. We could put inside of our setTimeout call the code
        // to re-find the #sent-results element, but that would be a bit
        // inelegant. Instead, we'll use a common JS idiom, to set a variable
        // to the *current* definition of self, here in this outer function,
        // so that the inner function can find it and where it will have the
        // same value. When stashing "this" into a new variable like that,
        // many JS programmers use the name "self"; some others use "that".
        var self = this;

        setTimeout(function () {
            $(self).slideUp();
        }, 2000);
    });
}